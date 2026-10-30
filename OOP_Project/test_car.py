class Car:
    def __init__(self, c='', t='', m='suv'):
        self.color = c
        self.type = t
        self.model = m

    def get_details(self):
        print('Car information')
        print('color:', self.color)
        print('type:', self.type)
        print('model:', self.model)


c1 = Car(c='red', t='petrol', m='test')
c1.get_details()