import os
from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel, Field

app = FastAPI(
    title="NetPulse Devices API",
    version="1.0.0",
    description="Module 2 applied project: secure Device Management API.",
)

ALGORITHM = "HS256"
ACCESS_TOKEN_MINUTES = 30

DEMO_USERNAME = os.getenv("DEMO_USERNAME")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")
JWT_SECRET = os.getenv("JWT_SECRET")

if not DEMO_USERNAME or not DEMO_PASSWORD or not JWT_SECRET:
    raise RuntimeError(
        "Set DEMO_USERNAME, DEMO_PASSWORD and JWT_SECRET environment variables before starting the app."
    )

password_hash = PasswordHash.recommended()
demo_user = {
    "username": DEMO_USERNAME,
    "password_hash": password_hash.hash(DEMO_PASSWORD),
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


class DeviceBase(BaseModel):
    name: str = Field(min_length=1)
    device_type: str = Field(min_length=1)
    status: str = Field(min_length=1)
    location: str = Field(min_length=1)


class DeviceCreate(DeviceBase):
    pass


class DeviceUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1)
    device_type: Optional[str] = Field(default=None, min_length=1)
    status: Optional[str] = Field(default=None, min_length=1)
    location: Optional[str] = Field(default=None, min_length=1)


class Device(DeviceBase):
    id: int


devices: dict[int, dict] = {
    1: {"id": 1, "name": "Router-01", "device_type": "router", "status": "online", "location": "Chennai-DC"},
    2: {"id": 2, "name": "Switch-01", "device_type": "switch", "status": "offline", "location": "Coimbatore-Branch"},
}
next_id = 3


def authenticate(username: str, password: str) -> bool:
    return (
        username == demo_user["username"]
        and password_hash.verify(password, demo_user["password_hash"])
    )


def create_access_token(subject: str) -> str:
    expires = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_MINUTES)
    return jwt.encode(
        {"sub": subject, "exp": expires},
        JWT_SECRET,
        algorithm=ALGORITHM,
    )


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not isinstance(username, str) or username != DEMO_USERNAME:
            raise credentials_error
        return username
    except InvalidTokenError:
        raise credentials_error


def get_device_or_404(device_id: int) -> dict:
    device = devices.get(device_id)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@app.get("/")
def home():
    return {"message": "NetPulse Devices API is running"}


@app.post("/auth/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    if not authenticate(form.username, form.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": create_access_token(form.username), "token_type": "bearer"}


@app.get("/devices", response_model=list[Device])
def list_devices():
    return list(devices.values())


@app.get("/devices/{device_id}", response_model=Device)
def get_device(device_id: int):
    return get_device_or_404(device_id)


@app.post("/devices", response_model=Device, status_code=status.HTTP_201_CREATED)
def create_device(device: DeviceCreate, current_user: str = Depends(get_current_user)):
    global next_id
    record = {"id": next_id, **device.model_dump()}
    devices[next_id] = record
    next_id += 1
    return record


@app.put("/devices/{device_id}", response_model=Device)
def replace_device(
    device_id: int,
    device: DeviceCreate,
    current_user: str = Depends(get_current_user),
):
    get_device_or_404(device_id)
    record = {"id": device_id, **device.model_dump()}
    devices[device_id] = record
    return record


@app.patch("/devices/{device_id}", response_model=Device)
def update_device(
    device_id: int,
    patch: DeviceUpdate,
    current_user: str = Depends(get_current_user),
):
    device = get_device_or_404(device_id)
    device.update(patch.model_dump(exclude_none=True))
    return device


@app.delete("/devices/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_device(device_id: int, current_user: str = Depends(get_current_user)):
    get_device_or_404(device_id)
    del devices[device_id]
    return None
