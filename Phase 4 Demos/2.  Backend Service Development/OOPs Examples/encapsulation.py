# Example of encapsulation in Python not to change the internal state directly as well as 
# through object 
class Product:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    def display(self):
        print(f"ID: {self.__id}, Name: {self.__name}")
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def set_id(self, id):
        if id > 0:
            self.__id = id
        else:
            print("Invalid ID. ID must be positive.")
    def set_name(self, name):
        self.__name = name
# Example usage
p1 = Product(100, "TV")
p1.display()
print(p1.get_id())
print(p1.get_name())
p1.set_id(-200)
p1.set_name("Laptop")
p1.display()