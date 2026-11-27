
import logging

import structlog
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from product_model import Product


logger = logging.getLogger(__name__)
structured_logger = structlog.get_logger(__name__)


class ProductRepository:

    # Store product in database
    def save_product(self, db: Session, product_data):
        logger.debug("Preparing product for database insert")
        structured_logger.debug("product_insert_preparing")
        product = Product(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            quantity=product_data.quantity
        )

        try:
            db.add(product)
            db.commit()
            db.refresh(product)
        except SQLAlchemyError:
            logger.exception("Product persistence failed; rolling back active transaction")
            structured_logger.exception(
                "product_persistence_failed", action="rollback_active_transaction"
            )
            db.rollback()
            raise

        logger.info("Product persisted: product_id=%s", product.id)
        structured_logger.info("product_persisted", product_id=product.id)
        return product


    # Retrieve all products
    def get_all_products(self, db: Session):
        logger.debug("Querying all products")
        structured_logger.debug("product_query_started")
        try:
            products = db.query(Product).all()
        except SQLAlchemyError:
            logger.exception("Product query failed")
            structured_logger.exception("product_query_failed")
            raise
        logger.info("Product query completed: count=%d", len(products))
        structured_logger.info("product_query_completed", count=len(products))
        return products
