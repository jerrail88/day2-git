# Day 8 - Exercise 4: Encapsulation Example

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

# Create object
account = BankAccount("Jerrail", 1000)

print(f"Owner: {account.owner}")
print(f"Balance: {account.get_balance()}")

account.deposit(500)
account.withdraw(300)
account.withdraw(1500)  # should fail
