
import logging

import structlog
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from product_schema import (
    ProductCreate,
    ProductResponse
)
from product_service import ProductService


logger = logging.getLogger(__name__)
structured_logger = structlog.get_logger(__name__)


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
    logger.info("Handling product creation")
    structured_logger.info("product_creation_handling")
    try:
        created = service.create_product(db, product)
        logger.info("Product creation completed: product_id=%s", created.id)
        structured_logger.info("product_creation_completed", product_id=created.id)
        return created

    except ValueError as e:
        logger.warning("Product creation rejected by business validation")
        structured_logger.warning(
            "product_creation_rejected", reason="business_validation"
        )
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# Retrieve All Products API
@router.get("/", response_model=list[ProductResponse])
def get_products(
    db: Session = Depends(get_db)
):
    logger.debug("Handling product listing")
    structured_logger.debug("product_listing_handling")
    return service.get_products(db)

