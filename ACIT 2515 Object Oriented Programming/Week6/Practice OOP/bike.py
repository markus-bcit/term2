

class Bike:
    def __init__(self):
        self.rider = None
        self.distance = 0
    def start_rental(self, name):
        if self.rider is not None:
            raise RuntimeError
        self.rider = name
    def bike(self, distance):
        if distance <= 0:
            raise AttributeError
        elif self.rider is None:
            raise RuntimeError
        self.distance += distance
    def end_rental(self):
        if self.rider is None:
            raise RuntimeError
        distance = self.distance
        self.distance = 0 
        self.rider = None
        return distance