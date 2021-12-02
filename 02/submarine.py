class Submarine:
    def __init__(self, use_aim=False):
        self.use_aim = use_aim
        self.coordinates = {"horizontal": 0, "depth": 0}
        self.aim = 0


    def move(self, direction, distance):
        if self.use_aim:
            if direction == "down":
                self.aim += distance

            if direction == "forward":
                self.coordinates["horizontal"] += distance
                self.coordinates["depth"] = self.aim * distance
        else:
            if direction == "forward":
                self.coordinates["horizontal"] += distance

            if direction == "down":
                self.coordinates["depth"] += distance

            if direction == "up":
                self.coordinates["depth"] -= distance
