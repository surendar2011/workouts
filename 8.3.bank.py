# BankAccount Class: Create a class BankAccount with attributes account_number and balance, and methods to deposit, withdraw, 
# and display the balance.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

# Creating an object and testing the methods
account1 = BankAccount("123456789", 1000.0)
account1.deposit(500)  # Depositing money
account1.withdraw(300)  # Withdrawing money
account1.withdraw(1500)  # Attempting to withdraw more than balance
