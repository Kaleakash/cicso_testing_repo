from typing import TypedDict

class Product(TypedDict):
    id: int
    name: str
    price: float

class ProductRepository:
    def __init__(self) -> None:
        self.products: list[Product] = []   # list of products

    # store a new product with name and price in memory and return it
    def store_product(self, name: str, price: float) -> Product:
        product: Product = {
            "id": len(self.products) + 1,
            "name": name,
            "price": price,
        }
        self.products.append(product)
        return product.copy()

    def get_all_products(self) -> list[Product]:
        return [product.copy() for product in self.products]