class Car:
    def get_details(self):
        # Note: self.color = '' was present in one revision, omit if setting externally:
        # self.color = ''
        print('Car information')
        print('color:', self.color)
        print('type:', self.type)
        print('model:', self.model)

# First instance
c1 = Car()
c1.color = 'red'
c1.type = 'petrol'
c1.model = 'suv'

c1.get_details()

# Second instance (if adding multiple cars)
c2 = Car()
c2.color = 'green'
c2.type = 'petrol'
c2.model = 'suv'

c2.get_details()