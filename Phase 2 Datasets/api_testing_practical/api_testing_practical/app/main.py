
from typing import Literal

from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Depends
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from pydantic import BaseModel, Field


# --------------------------------------------------
# 1. FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="Device Management Training API",
    description="REST API for Postman, Pytest, Newman and Locust testing.",
    version="1.0.0"
)


# --------------------------------------------------
# 2. In-Memory Database
# --------------------------------------------------

devices = {
    101: {
        "device_id": 101,
        "hostname": "edge-01",
        "status": "online"
    },
    102: {
        "device_id": 102,
        "hostname": "edge-02",
        "status": "offline"
    }
}


# --------------------------------------------------
# 3. Demo Authentication Configuration
# --------------------------------------------------

DEMO_TOKEN = "training-demo-token"

security = HTTPBearer(auto_error=False)


# --------------------------------------------------
# 4. Pydantic Request Model
# --------------------------------------------------

class DeviceCreate(BaseModel):

    hostname: str = Field(
        min_length=1,
        examples=["edge-03"]
    )

    status: Literal["online", "offline"] = "online"


# --------------------------------------------------
# 5. Health Check API
# --------------------------------------------------

@app.get("/")
def health_check():

    return {
        "message": "Device API is running",
        "status": "UP"
    }


# --------------------------------------------------
# 6. GET - Retrieve All Devices
# --------------------------------------------------

@app.get("/devices")
def get_devices():

    return list(devices.values())


# --------------------------------------------------
# 7. GET - Retrieve Device By ID
# --------------------------------------------------

@app.get("/devices/{device_id}")
def get_device(device_id: int):

    device = devices.get(device_id)

    if device is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device {device_id} not found"
        )

    return device


# --------------------------------------------------
# 8. POST - Create New Device
# --------------------------------------------------

@app.post(
    "/devices",
    status_code=status.HTTP_201_CREATED
)
def create_device(payload: DeviceCreate):

    # Check duplicate hostname

    for device in devices.values():

        if device["hostname"] == payload.hostname:

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A device with this hostname already exists"
            )

    # Generate next device ID

    next_id = max(devices.keys(), default=100) + 1

    new_device = {
        "device_id": next_id,
        "hostname": payload.hostname,
        "status": payload.status
    }

    devices[next_id] = new_device

    return new_device


# --------------------------------------------------
# 9. POST - Generate Demo Access Token
# --------------------------------------------------

@app.post("/auth/token")
def create_demo_token():

    return {
        "access_token": DEMO_TOKEN,
        "token_type": "bearer"
    }


# --------------------------------------------------
# 10. Authentication Dependency
# --------------------------------------------------

def verify_token(
    credentials: HTTPAuthorizationCredentials | None =
        Depends(security)
):

    # Check whether token is provided

    if credentials is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing bearer token",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # Extract actual token

    token = credentials.credentials

    # Validate token

    if token != DEMO_TOKEN:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid bearer token",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return token


# --------------------------------------------------
# 11. Protected API - Retrieve All Devices
# --------------------------------------------------

@app.get("/protected/devices")
def get_protected_devices(
    token: str = Depends(verify_token)
):

    return {
        "message": "Authentication successful",
        "devices": list(devices.values())
    }
