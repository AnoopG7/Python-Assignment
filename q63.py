# Create a class with a private attribute _balance and provide get_balance() and set_balance() methods.
class Account:
    def __init__(self):
        self._balance = 0  

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid balance amount. Balance cannot be negative.")

# Example usage
account = Account()
account.set_balance(1000)
print("Balance:", account.get_balance())
account.set_balance(-500)       #invalid balance example
