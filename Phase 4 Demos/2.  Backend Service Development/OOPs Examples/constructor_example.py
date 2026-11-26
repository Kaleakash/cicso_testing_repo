class Product:
    def __init__(abc, id, name):
        abc.id = id
        abc.name = name
        print("Product created")
    def display(abc):
        print("Displaying product details")
        print(f"ID: {abc.id}, Name: {abc.name}")


def info():
    print("Product information")

p1 = Product(100,"TV")
p1.display()

#info()