
class User:
    # Class Variable
    count = 10

    # Constructor
    def __init__(self):
        # Instance Variables
        self.first_name = ''
        self.last_name = ''

    # Instance Method
    def get_details(self):
        print('User information:', self.first_name, self.last_name)

    # Class Method
    @classmethod
    def test_class_method(cls):
        print('This is class method')

    # Static Method
    @staticmethod
    def test_static_method():
        print('This is static method')


# Object 1
u = User()
u.first_name = 'abc'
u.last_name = 'xyz'
u.get_details()

# Object 2
u1 = User()
u1.get_details()

# Class Variable access
print(User.count)

# Call Class Method
User.test_class_method()

# Call Static Method
User.test_static_method()
