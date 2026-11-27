
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from product_schema import (
    ProductCreate,
    ProductResponse
)
from product_service import ProductService


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

service = ProductService()


# Store Product API
@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    try:
        return service.create_product(db, product)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# Retrieve All Products API
@router.get("/", response_model=list[ProductResponse])
def get_products(
    db: Session = Depends(get_db)
):

    return service.get_products(db)
