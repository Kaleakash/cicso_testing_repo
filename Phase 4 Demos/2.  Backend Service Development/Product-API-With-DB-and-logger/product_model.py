
import logging

import structlog
from sqlalchemy import Column, Integer, String, Float
from db import Base


logger = logging.getLogger(__name__)
structured_logger = structlog.get_logger(__name__)


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    description = Column(String(255))

    price = Column(Float, nullable=False)

    quantity = Column(Integer, nullable=False)


logger.debug("Product ORM mapping defined: table=%s", Product.__tablename__)
structured_logger.debug("product_mapping_defined", table=Product.__tablename__)

