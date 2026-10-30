class Car:
    def __init__(self):
        # print('car init method / constructor')
        self.color = ''
        self.type = ''
        self.model = ''

    def get_details(self):
        print('Car information')
        print('color:', self.color)
        print('type:', self.type)
        print('model:', self.model)


c1 = Car()
c1.color = 'black'
c1.type = 'electric'
c1.model = 'suv'

c1.get_details()