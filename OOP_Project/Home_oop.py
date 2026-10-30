class Room:
    def __init__(self):
        self.room1_colour = ''
        self.room2_colour = ''
        self.hall_colour = ''
    def room_colour_info(self):
        print('room1_colour:-',self.room1_colour)
        print('room2_colour:-', self.room2_colour)
        print('Hall_colour:-', self.hall_colour)

r=Room()
r.room1_colour='Red and Green'
r.room2_colour='blue and white'
r.hall_colour='only pink'
r.room_colour_info()
