# Demonstrate encapsulation by creating a class with private attributes and use getter and setter methods to access/modify them.
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount.")

account = Account(100)
print("Initial balance:", account.get_balance())
account.set_balance(150)
print("Updated balance:", account.get_balance())
