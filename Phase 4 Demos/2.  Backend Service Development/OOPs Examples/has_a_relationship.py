# example using aggregation
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}, Engine Horsepower: {self.engine.horsepower}")

# Example usage
engine = Engine(150)
car = Car("Toyota", "Corolla", engine)
car.display_info()
# example using composition
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

class ElectricCar:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def display_info(self):
        print(f"Electric Car Brand: {self.brand}, Model: {self.model}, Battery Capacity: {self.battery.capacity} kWh")

# Example usage
battery = Battery(100)
electric_car = ElectricCar("Tesla", "Model S", battery)
electric_car.display_info()