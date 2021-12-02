class Submarine:
    def __init__(self):
        self.coordinates = {"horizontal": 0, "depth": 0}


    def move(self, direction, distance):
        if direction == "forward":
            self.coordinates["horizontal"] += distance

        if direction == "down":
            self.coordinates["depth"] += distance

        if direction == "up":
            self.coordinates["depth"] -= distance
