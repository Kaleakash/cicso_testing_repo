from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field

from productRepository import Product
from productService import ProductService


class ProductCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(ge=0, allow_inf_nan=False)


class ProductResponse(ProductCreate):
    id: int


router = APIRouter(prefix="/products", tags=["products"])
product_service = ProductService()


def get_product_service() -> ProductService:
    return product_service


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def store_product(
    product: ProductCreate,
    service: Annotated[ProductService, Depends(get_product_service)],
) -> Product:
    try:
        return service.store_product(product.name, product.price)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=str(error)
        ) from error


@router.get("", response_model=list[ProductResponse])
def get_all_products(
    service: Annotated[ProductService, Depends(get_product_service)],
) -> list[Product]:
    return service.get_all_products()
