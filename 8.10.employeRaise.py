# Employee Class: Create a class Employee with a method to calculate the yearly salary, give a raise, and display details.

class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_yearly_salary(self):
        return self.monthly_salary * 12

    def give_raise(self, amount):
        self.monthly_salary += amount
        print(f"{self.name} received a raise of {amount}. New monthly salary: {self.monthly_salary}")

# Creating an object and testing the methods
employee1 = Employee("Alice", 5000)

print(f"Yearly Salary before raise: {employee1.calculate_yearly_salary()}")  
employee1.give_raise(500)  # Giving a raise of 500
print(f"Yearly Salary after raise: {employee1.calculate_yearly_salary()}")
