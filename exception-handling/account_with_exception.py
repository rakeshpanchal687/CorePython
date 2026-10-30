class InsufficientFundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Account:
    def __int__(self):
        self.balance = 0

    def set_setbalance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 1000:
            self.balance -= amount
        else:
            raise InsufficientFundException("Insufficient funds. Minimum balance of 1000 must be maintained.")


acc = Account()
acc.set_setbalance(5000)

try:
    acc.deposit(5000)
    acc.withdraw(1000)
    acc.withdraw(2000)
except InsufficientFundException as e:
    print("exception:", e)
    # acc.deposit(5000)
