"""Cisco M2S2 Demo 01: beginner Product CRUD API (in-memory storage)."""
from typing import Optional

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, Field

app = FastAPI(
    title="Product API",
    version="1.0.0",
    description="Beginner CRUD API used in the Cisco AI Apprenticeship FastAPI lab.",
)


class ProductBase(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(ge=0)
    in_stock: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1)
    price: Optional[float] = Field(default=None, ge=0)
    in_stock: Optional[bool] = None


class Product(ProductBase):
    id: int


products: dict[int, Product] = {
    1: Product(id=1, name="Keyboard", price=30.0, in_stock=True),
    2: Product(id=2, name="Mouse", price=15.0, in_stock=True),
}
next_id = 3


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"message": exc.detail, "status": exc.status_code}},
        headers=exc.headers,
    )


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/products", response_model=list[Product])
def list_products():
    return list(products.values())


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate):
    global next_id
    product = Product(id=next_id, **payload.model_dump())
    products[next_id] = product
    next_id += 1
    return product


@app.put("/products/{product_id}", response_model=Product)
def replace_product(product_id: int, payload: ProductCreate):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    product = Product(id=product_id, **payload.model_dump())
    products[product_id] = product
    return product


@app.patch("/products/{product_id}", response_model=Product)
def update_product(product_id: int, payload: ProductUpdate):
    existing = products.get(product_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Product not found")
    updates = payload.model_dump(exclude_unset=True)
    product = existing.model_copy(update=updates)
    # Validate the assembled product, including any explicitly supplied nulls.
    product = Product.model_validate(product.model_dump())
    products[product_id] = product
    return product


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    del products[product_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
