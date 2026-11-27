from productRepository import Product, ProductRepository


class ProductService:
    def __init__(self) -> None:
        self.product_repository = ProductRepository()

    def store_product(self, name: str, price: float) -> Product:
        if not price > 1000:
            raise ValueError("Product price must be greater than 1000.")
        return self.product_repository.store_product(name, price)

    def get_all_products(self) -> list[Product]:
        products = self.product_repository.get_all_products()
        for product in products:
            product["price"] = product["price"] * 0.9
        return products