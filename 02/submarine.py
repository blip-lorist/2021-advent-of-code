class Submarine:
    def __init__(self):
        self.coordinates = {"horizontal": 0 }


    def move(self, direction, distance):
        if direction == "forward":
            self.coordinates["horizontal"] += distance

