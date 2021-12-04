import numpy as np
from collections import Counter

class BingoBoard:
    def __init__(self, values):
        self.values = values
        self.last_number_checked = None
        self.marked_coordinates = []

    def mark_tile(self, value):
        values_ndarray = np.array(self.values)
        coordinates = zip(*np.where(values_ndarray == value))
        self.marked_coordinates += coordinates
        self.last_number_checked = value

    def has_win(self):
        # Win if any x coordinate has a count of 5
        # or if any y coordinate has a count of 5
        counter = {
            "x": Counter(),
            "y": Counter(),
            }

        for coordinate in self.marked_coordinates:
            x = coordinate[0]
            y = coordinate[1]
            counter["x"][x] += 1
            counter["y"][y] += 1

        for coordinate, count in counter["x"].items():
            if count == 5:
                return True

        for coordinate, count in counter["y"].items():
            if count == 5:
                return True

        return False
