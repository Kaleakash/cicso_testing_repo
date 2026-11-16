
import os
import httpx


# Base URL of the FastAPI application
BASE_URL = os.getenv(
    "BASE_URL",
    "http://127.0.0.1:8000"
)


# Test 1: Protected API with a valid token
def test_protected_devices_with_valid_token():

    # Step 1: Generate/Get access token
    token_response = httpx.post(
        f"{BASE_URL}/auth/token",
        timeout=5.0
    )

    assert token_response.status_code == 200

    token_data = token_response.json()
    token = token_data["access_token"]

    # Step 2: Pass token in Authorization header
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Step 3: Access protected endpoint
    response = httpx.get(
        f"{BASE_URL}/protected/devices",
        headers=headers,
        timeout=5.0
    )

    # Step 4: Validate response
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert data["message"] == "Authentication successful"
    assert isinstance(data["devices"], list)
    assert len(data["devices"]) >= 1


# Test 2: Protected API without a token
def test_protected_devices_without_token():

    # Step 1: Call protected endpoint without Authorization header
    response = httpx.get(
        f"{BASE_URL}/protected/devices",
        timeout=5.0
    )

    # Step 2: Validate unauthorized response
    assert response.status_code == 401

    # Step 3: Validate error message
    assert response.json()["detail"] == "Missing bearer token"


# Test 3: Protected API with an invalid token
def test_protected_devices_with_invalid_token():

    # Step 1: Prepare invalid token
    headers = {
        "Authorization": "Bearer invalid-token"
    }

    # Step 2: Call protected endpoint
    response = httpx.get(
        f"{BASE_URL}/protected/devices",
        headers=headers,
        timeout=5.0
    )

    # Step 3: Validate unauthorized response
    assert response.status_code == 401

    # Step 4: Validate error message
    assert response.json()["detail"] == "Invalid bearer token"
