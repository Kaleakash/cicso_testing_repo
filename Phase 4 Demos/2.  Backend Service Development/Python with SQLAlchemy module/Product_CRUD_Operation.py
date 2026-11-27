import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)


# provide us database details like sqlite, postgresql, mysql etc.
engine = sqlalchemy.create_engine("sqlite:///products.db")
# create all tables defined by the Base's subclasses
Base.metadata.create_all(engine)

# Now you can use the engine to interact with the database, for example, creating a session to add or query products.

Session = sessionmaker(bind=engine)
# this session reference provide us function to interact with database to 
# store, delete, update and retrieve records from the database without writing sql native query 
session = Session()

def add_product(name, price):
    try:
        new_product = Product(name=name, price=price)
        session.add(new_product)        # is equal to insert query in SQL
        session.commit()                # this line commits the transaction to the database
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
        return False
    return True

def get_all_products():
    try:
        # it is equal to select query 
        products = session.query(Product).all()  # this line queries all products from the database
        return products
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
# delete product by id
# need confirmation after delete success
def delete_product(product_id):
    try:
        # retrieve the product by id from the database
        product = session.query(Product).filter(Product.id == product_id).first()
        if product:
            session.delete(product) # delete from product where id = product_id
            session.commit()
            return True
        else:
            print("Product not found.")
            return False
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
        return False
    
# update product by id

# update product by id with confirmation
def update_product(product_id, name=None, price=None):
    try:
        product = session.query(Product).filter(Product.id == product_id).first()
        if product:
            if name:
                product.name = name
            if price:
                product.price = price
            session.commit()
            return True
        else:
            print("Product not found.")
            return False
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
        return False

# need logic to take the value through keyboard inside while with switch statement 
def menu():
    print("1. Add Product")
    print("2. View All Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def main(): 
    while True:
        choice = menu()
        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            add_product(name, price)
        elif choice == "2":
            products = get_all_products()
            for product in products:
                print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")
        elif choice == "3":
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            price_input = input("Enter new price (leave blank to keep current): ")
            price = float(price_input) if price_input else None
            if update_product(product_id, name=name if name else None, price=price):
                print("Product updated successfully.")
            else:
                print("Failed to update product.")
        elif choice == "4":
            product_id = int(input("Enter product ID to delete: "))
            if delete_product(product_id):
                print("Product deleted successfully.")
            else:
                print("Failed to delete product.")
        elif choice == "5": 
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()