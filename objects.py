class point_Charge:

    def __init__(self, charge, coordinates):
        self.charge = charge
        self.coordinates = coordinates

class Charges:

    def __init__(self):
        self.charges = []
        self.length = 0

    def add_Charges(self, charge, coordinates):
        self.charges.append(point_Charge(charge, coordinates))
        self.length += 1


