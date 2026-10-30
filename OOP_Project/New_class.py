class Employee:

    def __init__(self):
        self.name = ''
        self.salary = 0
        self.department = ''

    def display_details(self):
        print('Employee Name:-',self.name)
        print('Employee Salary:-',self.salary)
        print('Employee Department:-',self.department)
        # print('User information:', '\n', self.name, '\n', self.salary, '\n', self.department)

    @classmethod
    def displaycompanyname(cls):
        print('Company name:-', 'Rays Technologies')

    @staticmethod
    def calculate_bonus():
        print('Yearly Bonus:-', 'Bonus is 10% of salary')


e = Employee()
e.name = 'Rakesh'
e.salary = 10000
e.department = 'IT'

e.display_details()
e.displaycompanyname()
e.calculate_bonus()
