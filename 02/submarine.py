class Submarine:
    def __init__(self):
        self.coordinates = {"horizontal": 0, "depth": 0}
        self.aim = 0


    def move(self, direction, distance, use_aim=False):
        if use_aim:
            if direction == "down":
                self.aim += distance
        else:
            if direction == "forward":
                self.coordinates["horizontal"] += distance

            if direction == "down":
                self.coordinates["depth"] += distance

            if direction == "up":
                self.coordinates["depth"] -= distance
