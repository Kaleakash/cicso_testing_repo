
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

FAKE_API = "https://jsonplaceholder.typicode.com"


@app.get("/")
async def home():
    return {
        "message": "FastAPI Asyncio HTTPX Application"
    }


@app.get("/users")
async def get_users():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{FAKE_API}/users"
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=502,
                detail="External API failed"
            )

        return response.json()

    
@app.get("/users/{user_id}")
async def get_user(user_id: int):

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{FAKE_API}/users/{user_id}"
        )

        if response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        response.raise_for_status()

        return response.json()
