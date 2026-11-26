# Below  is an example of inheritance
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        print(f"Electric Car Brand: {self.brand}, Model: {self.model}, Battery Capacity: {self.battery_capacity} kWh")

# Example usage
car = Car("Toyota", "Corolla")
car.display_info()

electric_car = ElectricCar("Tesla", "Model S", 100)
electric_car.display_info()


# polymorphism example with function overloading and overriding
class Bike:
    def speed(self):
        print("Bike is moving at a certain speed")

class SportsBike(Bike):
    def speed(self):
        print("Sports Bike is moving at a high speed")
    # def speed(self, speed_value):
    #     print(f"Sports Bike is moving at a speed of {speed_value} km/h")

# Example usage
bike = Bike()
bike.speed()

sports_bike = SportsBike()
sports_bike.speed()  
# sports_bike.speed(120)