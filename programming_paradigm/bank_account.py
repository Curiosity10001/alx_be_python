class BankAccount:  # Creates empty non active class ; this line alone is like a empty placeholder
    def __init__(self, initial_balance=0):  # initial balance 0
        self.account_balance = initial_balance  # create the attribute and assign initial balance to it

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance - amount >= 0:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
