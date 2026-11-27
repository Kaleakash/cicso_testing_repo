
from product_repository import ProductRepository


class ProductService:

    def __init__(self):

        self.repository = ProductRepository()


    # Business logic for storing product
    def create_product(self, db, product_data):

        # Business validation
        if product_data.price <= 0:
            raise ValueError("Price must be greater than zero")

        if product_data.quantity < 0:
            raise ValueError("Quantity cannot be negative")

        return self.repository.save_product(
            db,
            product_data
        )


    # Business logic for retrieving products
    #  need condition to apply discount as 10% for all product 
    def get_products(self, db):

        products = self.repository.get_all_products(db)

        # Apply 10% discount to all products
        for product in products:
            product.price = product.price * 0.9

        return products
