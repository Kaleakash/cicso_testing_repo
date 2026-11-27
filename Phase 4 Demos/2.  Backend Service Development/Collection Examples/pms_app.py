# in memory data for products
list_of_products=[
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500},
    {"id": 3, "name": "Tablet", "price": 300}   
]
# business function to display all products 
def view_products():
    for product in list_of_products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")

def add_product(id, name, price):
    # business function to add a new product with id must be unique 
    for product in list_of_products:
        if product['id'] == id:
            print("Error: Product with this ID already exists.")
            return
    list_of_products.append({"id": id, "name": name, "price": price})
    print("Product added successfully.")


def delete_product(id):
    # business function to delete a product by id
    for product in list_of_products:
        if product['id'] == id:
            list_of_products.remove(product)
            print("Product deleted successfully.")
            return
    print("Error: Product with this ID does not exist.")    

def update_product(id, name, price):
    # business function to update a product by id
    for product in list_of_products:
        if product['id'] == id:
            product['name'] = name
            product['price'] = price
            print("Product updated successfully.")
            return
    print("Error: Product with this ID does not exist.")




# need code to call all function in do while with switch statement 
while True:
    print("\n1. View Products")
    print("2. Add Product")
    print("3. Delete Product")
    print("4. Update Product")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        view_products()
    elif choice == "2":
        id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        add_product(id, name, price)
    elif choice == "3":
        id = int(input("Enter product ID to delete: "))
        delete_product(id)
    elif choice == "4":
        id = int(input("Enter product ID to update: "))
        name = input("Enter new product name: ")
        price = float(input("Enter new product price: "))
        update_product(id, name, price)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")