# Car Class: Create a class Car with attributes brand and model, and a method to display the car’s full details.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Creating an object of the Car class
car1 = Car("Toyota", "Corolla")

# Printing the attributes
print(f"Brand: {car1.brand}")
print(f"Model: {car1.model}")
