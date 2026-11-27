
from pydantic import BaseModel, Field, ConfigDict


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
