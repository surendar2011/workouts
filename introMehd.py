class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    
# creating an object and calling the method

person1 = Person("Alice", 21)
person1.introduce()