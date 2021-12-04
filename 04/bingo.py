import numpy as np

class BingoBoard:
    def __init__(self, values):
        self.values = values
        self.marked_coordinates = []

    def mark_tile(self, value):
        values_ndarray = np.array(self.values)
        coordinates = zip(*np.where(values_ndarray == value))
        print(coordinates)
        self.marked_coordinates += coordinates

