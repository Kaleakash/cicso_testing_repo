
import os
from uuid import uuid4

import httpx

BASE_URL = os.getenv(
    "BASE_URL",
    "http://127.0.0.1:8000"
)


def test_get_devices():

    response = httpx.get(
        f"{BASE_URL}/devices",
        timeout=5.0
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_existing_device():

    response = httpx.get(
        f"{BASE_URL}/devices/101",
        timeout=5.0
    )

    assert response.status_code == 200

    data = response.json()

    assert data["device_id"] == 101
    assert data["hostname"] == "edge-01"
    assert data["status"] == "online"


def test_get_missing_device():

    response = httpx.get(
        f"{BASE_URL}/devices/99999",
        timeout=5.0
    )

    assert response.status_code == 404


def test_create_device():

    hostname = f"training-{uuid4().hex[:8]}"

    payload = {
        "hostname": hostname,
        "status": "online"
    }

    response = httpx.post(
        f"{BASE_URL}/devices",
        json=payload,
        timeout=5.0
    )

    assert response.status_code == 201

    data = response.json()

    assert data["hostname"] == hostname
    assert data["status"] == "online"
    assert isinstance(data["device_id"], int)
