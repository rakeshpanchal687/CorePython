class BankAccount:


    def __init__(self):
        self.account_holder =''
        self.balance = ''
        self.account_number = ''

    def get_account_details(self):
        print('Account Holder:-', self.account_holder)
        print('Account Balance:-', self.balance)
        print('Account Number:-', self.account_number)

    def display_balance():
        print('Account Balance:-', self.balance)

    @classmethod
    def display_bank_name(cls):
        print('Bank Name:-', 'HDFC Bank')

    @staticmethod
    def validate_account_number():
        print('Account Number Validation:-', '253637484')

b=BankAccount()
b.account_holder='Rakesh'
b.balance=10000
b.account_number='253637484'
b.get_account_details()


