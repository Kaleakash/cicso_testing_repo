class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

p1 = Product("Laptop", 1000, 2)
p2 = Product("Phone", 500, 3)
p3 = Product("Tablet", 300, 4)

print(p1)   # Print product details for p1  it call __str__ method
print(p2)   # Print product details for p2  it call __str__ method
print(p3)   # Print product details for p3  it call __str__ method

print(p1.get_total_price())   # Print total price for p1  it call get_total_price method
print(p2.get_total_price())   # Print total price for p2  it call get_total_price method
print(p3.get_total_price())   # Print total price for p3  it call get_total_price method