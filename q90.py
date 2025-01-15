# Modify the Car class to have default values for make and model if not provided.
class Car:
    def __init__(self, make="Ford", model="Focus", year=2000):
        self.make = make
        self.model = model
        self.year = year

car1 = Car()
car2 = Car("Tesla", "Model S", 2022)
print(f"Default car: {car1.year} {car1.make} {car1.model}")
print(f"Custom car: {car2.year} {car2.make} {car2.model}")
