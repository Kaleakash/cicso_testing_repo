
from fastapi import FastAPI

from db import engine, Base

from product_model import Product

from product_controller import router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Product Management API",
    description="FastAPI + SQLAlchemy + SQLite",
    version="1.0"
)


# Register product controller
app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Product Management API is running"
    }
