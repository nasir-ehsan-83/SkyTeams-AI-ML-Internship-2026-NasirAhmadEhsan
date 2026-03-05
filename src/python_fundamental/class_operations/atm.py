# a simple menu-based ATM
class ATM:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount
        return f"{amount} deposited successfully"
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance -= amount
        return f"{amount} withdrawn successfully"
    
    def get_balance(self):
        return self.__balance