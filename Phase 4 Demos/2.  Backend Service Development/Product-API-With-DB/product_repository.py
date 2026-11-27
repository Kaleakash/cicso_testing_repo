
from sqlalchemy.orm import Session
from product_model import Product


class ProductRepository:

    # Store product in database
    def save_product(self, db: Session, product_data):

        product = Product(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            quantity=product_data.quantity
        )

        db.add(product)

        db.commit()

        db.refresh(product)

        return product


    # Retrieve all products
    def get_all_products(self, db: Session):

        return db.query(Product).all()
