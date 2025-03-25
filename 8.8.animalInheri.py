# Animal Inheritance: Create a parent class Animal with a speak() method. 
# Create child classes Dog and Cat that inherit from Animal and override speak().

'''
What is Inheritance? 🏛️
Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a child class to inherit properties and methods from a parent class.

🔹 Key Idea:
Instead of writing the same code multiple times, you define common behavior in a parent class and let child classes inherit and extend it.

'''


class Animal:
    def speak(self):
        return "Animal makes a sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

# Creating objects of Cat and Dog and calling speak
cat1 = Cat()
dog1 = Dog()

print(cat1.speak())  # Output: Meow
print(dog1.speak())  # Output: Woof
