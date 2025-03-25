# Person Class: Create a class Person with attributes name and age, and methods to introduce the person, update the age, 
# and determine if they are an adult.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example usage
person1 = Person("Alice", 30)
person1.display_info()

# ----------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of the Person class
person1 = Person("Alice", 30)

# Printing the attributes
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
