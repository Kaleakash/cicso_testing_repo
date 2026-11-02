from typing import Optional
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(title="Device Management API", version="1.0.0", description="Beginner FastAPI CRUD solution for the Cisco AI Apprenticeship practice.")

class DeviceBase(BaseModel):
    name: str = Field(min_length=1)
    device_type: str = Field(min_length=1)
    status: str = Field(min_length=1)

class DeviceCreate(DeviceBase):
    pass

class DeviceUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1)
    device_type: Optional[str] = Field(default=None, min_length=1)
    status: Optional[str] = Field(default=None, min_length=1)

class Device(DeviceBase):
    id: int

devices: dict[int, dict] = {
    1: {"id": 1, "name": "Router-01", "device_type": "router", "status": "online"},
    2: {"id": 2, "name": "Switch-01", "device_type": "switch", "status": "offline"},
}
next_id = 3

@app.exception_handler(StarletteHTTPException)
async def http_error_handler(request: Request, exc: StarletteHTTPException):
    code = "DEVICE_NOT_FOUND" if exc.status_code == 404 else "HTTP_ERROR"
    return JSONResponse(status_code=exc.status_code, content={"error": {"code": code, "message": str(exc.detail), "status": exc.status_code}})

@app.get("/")
def home():
    return {"message": "Device API is running"}

@app.get("/devices", response_model=list[Device])
def list_devices():
    return list(devices.values())

@app.get("/devices/{device_id}", response_model=Device)
def get_device(device_id: int):
    device = devices.get(device_id)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@app.post("/devices", response_model=Device, status_code=status.HTTP_201_CREATED)
def create_device(device: DeviceCreate):
    global next_id
    record = {"id": next_id, **device.model_dump()}
    devices[next_id] = record
    next_id += 1
    return record

@app.put("/devices/{device_id}", response_model=Device)
def replace_device(device_id: int, device: DeviceCreate):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    record = {"id": device_id, **device.model_dump()}
    devices[device_id] = record
    return record

@app.patch("/devices/{device_id}", response_model=Device)
def update_device(device_id: int, patch: DeviceUpdate):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    updates = patch.model_dump(exclude_none=True)
    devices[device_id].update(updates)
    return devices[device_id]

@app.delete("/devices/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_device(device_id: int):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    del devices[device_id]
    return None
