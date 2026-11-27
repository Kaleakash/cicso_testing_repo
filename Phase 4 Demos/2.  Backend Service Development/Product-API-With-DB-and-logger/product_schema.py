
import logging

import structlog
from pydantic import BaseModel, Field, ConfigDict


logger = logging.getLogger(__name__)
structured_logger = structlog.get_logger(__name__)


# Incoming request
class ProductCreate(BaseModel):

    name: str = Field(min_length=2, max_length=100)

    description: str | None = Field(default=None, max_length=255)

    price: float = Field(gt=0)

    quantity: int = Field(ge=0)


# Outgoing response
class ProductResponse(BaseModel):

    id: int

    name: str

    description: str | None

    price: float

    quantity: int

    model_config = ConfigDict(from_attributes=True)


logger.debug("Product request and response schemas defined")
structured_logger.debug("product_schemas_defined")

