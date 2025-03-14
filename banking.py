class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"withdred ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid ammount.")

account1 = BankAccount("12345679", 1000.00)
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)