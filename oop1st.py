class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Printing the attributes
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the Person class
person1 = Person("Alice", 21)
person1.display_info()