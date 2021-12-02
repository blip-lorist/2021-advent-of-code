import sys
import os.path
from depth_increases import count_increases

def part_one():
    with open("puzzle_input", "r") as input_file:
        string_list = input_file.readlines()

        num_list = [int(x) for x in string_list]
        total = count_increases(num_list)
        print(total)

part_one()

