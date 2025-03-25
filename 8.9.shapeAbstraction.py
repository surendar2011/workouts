# Shape Abstraction: Create a base class Shape with an abstract method area(). Create subclasses Square and Triangle that implement area().

'''
Why Use Abstract Methods?
✅ Forces subclasses to implement important methods (e.g., every shape must have an area()).
✅ Prevents creating incomplete objects (you cannot create a Shape without area()).
✅ Encourages consistency across different subclasses.

'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Example of a subclass implementing the area method
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating an object and testing the area method
rect1 = Rectangle(10, 5)
print(f"Area of rectangle: {rect1.area()}")  # Output: 50
