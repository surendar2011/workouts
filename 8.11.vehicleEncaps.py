# Vehicle Encapsulation: Create a class Vehicle with private attributes and methods to access and modify them.


'''
What is Encapsulation? 🔒
Encapsulation is an Object-Oriented Programming (OOP) principle that restricts direct access to an object’s data and modifies it only through controlled methods (getters and setters).

🔹 Key Idea:

Protect sensitive data by making attributes private (__attribute).
Use getter methods (get_*()) to access data.
Use setter methods (set_*()) to modify data safely.


 Key Takeaways
1️⃣ Private attributes (__attribute) cannot be accessed directly.
2️⃣ Getters allow safe data retrieval.
3️⃣ Setters allow controlled modification.
4️⃣ Prevents invalid or harmful data changes.

'''

class Vehicle:
    def __init__(self, brand, model, year):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute
        self.__year = year    # Private attribute

    # Getter methods
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Setter methods
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        if year > 1885:  # Cars were invented around 1886
            self.__year = year
        else:
            print("Invalid year!")

    def get_details(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Year: {self.__year}"

# Creating an object and testing methods
vehicle1 = Vehicle("Toyota", "Corolla", 2022)

# Accessing private attributes using getters
print(vehicle1.get_details())  

# Modifying private attributes using setters
vehicle1.set_brand("Honda")
vehicle1.set_model("Civic")
vehicle1.set_year(2025)  # Valid update

print(vehicle1.get_details())  

# Trying to set an invalid year
vehicle1.set_year(1800)  # Output: Invalid year!

# -------------------------------------------------------------------------------------------

class Vehicle:
    def __init__(self, brand, model, year):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute
        self.__year = year    # Private attribute

# Creating an object
car = Vehicle("Toyota", "Corolla", 2022)

# Trying to access private attributes directly
print(car.__brand)  # ❌ ERROR: AttributeError
print(car.__model)  # ❌ ERROR: AttributeError
print(car.__year)   # ❌ ERROR: AttributeError

# -------------------------------------------------------------------------------------------

# Using Getter Methods
print(car.get_brand())  # ✅ Output: Toyota
print(car.get_model())  # ✅ Output: Corolla
print(car.get_year())   # ✅ Output: 2022
