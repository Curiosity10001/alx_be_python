class BankAccount: #Creates empty non active class ; this line alone is like a empty placeholder
	def __init__(self, initial_balance = 0): #intial balance 0
		self.account_balance = initial_balance #creating the modifiable parameter and assining the initial balance to it

	def deposit(self,amount):
		account_balance += amount

	def withdraw(self,amount):
		if account_balance - amount>=0 :
		account_balance -= amount
		return True
		else False

	def display_balance(self):
		print(f'Current Balance: $'{self._account_balance})