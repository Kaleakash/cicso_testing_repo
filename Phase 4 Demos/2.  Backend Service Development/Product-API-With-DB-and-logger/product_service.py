
import logging

import structlog
from product_repository import ProductRepository


logger = logging.getLogger(__name__)
structured_logger = structlog.get_logger(__name__)


class ProductService:

    def __init__(self):
        logger.debug("Initializing product service")
        structured_logger.debug("product_service_initializing")
        self.repository = ProductRepository()


    # Business logic for storing product
    def create_product(self, db, product_data):
        logger.info("Validating product creation")
        structured_logger.info("product_creation_validating")
        # Business validation
        if product_data.price <= 0:
            logger.warning("Product creation rejected: price must be greater than zero")
            structured_logger.warning(
                "product_creation_rejected", reason="price_must_be_positive"
            )
            raise ValueError("Price must be greater than zero")

        if product_data.quantity < 0:
            logger.warning("Product creation rejected: quantity cannot be negative")
            structured_logger.warning(
                "product_creation_rejected", reason="quantity_must_be_nonnegative"
            )
            raise ValueError("Quantity cannot be negative")

        return self.repository.save_product(
            db,
            product_data
        )


    # Business logic for retrieving products
    #  need condition to apply discount as 10% for all product 
    def get_products(self, db):
        logger.info("Retrieving products for discounted response")
        structured_logger.info("discounted_products_retrieving")
        products = self.repository.get_all_products(db)

        # Apply 10% discount to all products
        for product in products:
            product.price = product.price * 0.9

        logger.info("Applied 10%% discount: product_count=%d", len(products))
        structured_logger.info(
            "product_discount_applied", discount_percent=10, product_count=len(products)
        )
        return products
