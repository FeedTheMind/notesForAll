# __init__ is an initializer. It sets up the objects with the values we pass when we create it.

class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print("Braking!")

# These are two instances of the Bike class
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')
