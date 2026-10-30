class Account:

    def __init__(self):
        self.bank_name = ''
        self.account_number = ''
        self.balance = 0

    def get_account_info(self):
        print('Bank Name:-', self.bank_name)
        print('Account Number:-', self.account_number)
        print('Balance:-', self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(amount, 'deopsit,update balance', self.balance)


    def witdrowl(self, amount):
      self.balance -= amount
      print(amount, 'withdrowl update balance', self.balance)


a = Account()
a.bank_name = 'sbi'
a.account_number = 'sbin1122333'
a.balance = 1000

a.deposit(4000)
a.witdrowl(243)
