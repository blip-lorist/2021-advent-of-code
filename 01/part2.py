import sys
import os.path
from depth_increases import window_sums_increases

def part_two():
    with open("puzzle_input", "r") as input_file:
        string_list = input_file.readlines()

        num_list = [int(x) for x in string_list]
        total = window_sums_increases(num_list)
        print(total)

part_two()

