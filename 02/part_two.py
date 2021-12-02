import sys
import os.path
from submarine import Submarine

def part_two():
    with open("puzzle_input", "r") as input_file:
        string_list = input_file.readlines()
        tuples = []
        new_submarine = Submarine(use_aim=True)

        for string_movement in string_list:
            direction, distance = string_movement.split(" ")
            direction_distance_tuple = (direction, int(distance))
            tuples.append(direction_distance_tuple)

        for movement in tuples:
            direction, distance = movement
            new_submarine.move(direction, distance)

        horizontal_depth_product = new_submarine.coordinates["horizontal"] * new_submarine.coordinates["depth"]
        print(horizontal_depth_product)

part_two()

