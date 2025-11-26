# Day 8 - Exercise 2: Methods and Updating Attributes

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print(f"You drove {miles} miles.")

    def get_description(self):
        return f"{self.year} {self.make} {self.model} with {self.mileage} miles"

# Create an object
my_car = Car("Toyota", "Camry", 2020)

print(my_car.get_description())
my_car.drive(50)
print(my_car.get_description())
