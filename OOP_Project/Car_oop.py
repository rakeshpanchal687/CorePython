class Car :
    def __init__(self):
        self.car_name=''
        self.car_colour=''
    def get_car_info(self):
        print('car name :-',self.car_name)
        print('car colour:-',self.car_colour)

c=Car()
c.car_name='Thar'
c.car_colour='black'
c.get_car_info()
