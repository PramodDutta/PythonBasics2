class BankAccount:
    def __init__(self):
        self.balance = 0  # Public Attribute

    def deposit(self, amount):
        self.balance += amount

    def _withdraw(self, amount): # Protected Attribute
        self.balance -= amount

    def ___show_balance(self):
        print("Balance is ", self.balance) # Private Attribute

    def is_Auth_True(self, isAuth):
        if isAuth:
            print("You are Auth!!")
            self.___show_balance()
        else:
            print("Not Auth, No Bal")

    def is_withdraw_Auth_True(self, isAuth_withdraw, amount):
        if isAuth_withdraw:
            print("You are Auth!!,WithDraw")
            self._withdraw(amount)
        else:
            print("Not Auth, No Bal")


account = BankAccount()
account.deposit(1000)
# account._withdraw(499) # Not a good practice
account.is_withdraw_Auth_True(True, 499)

# Auth - UP

account.is_Auth_True(False)
