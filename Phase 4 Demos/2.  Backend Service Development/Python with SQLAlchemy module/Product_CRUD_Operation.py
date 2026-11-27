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

# need logic to take the value through keyboard inside while with switch statement 
def menu():
    print("1. Add Product")
    print("2. View All Products")
    print("3. Exit")
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
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()