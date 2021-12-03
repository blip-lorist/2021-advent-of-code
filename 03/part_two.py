import sys
import os.path
from bit_array import BitArray

def part_two():
    with open("puzzle_input", "r") as input_file:
        string_list = input_file.readlines()

    int_lists = []
    for bits in string_list:
        bits_int_list = [int(x) for x in bits.strip()]
        int_lists.append(bits_int_list)

    oxygen_bit_array = BitArray(int_lists)
    oxygen_bit_array.compute_oxygen_generator_rating()
    oxygen_rating = oxygen_bit_array.decimal_oxygen_rating

    co2_bit_array = BitArray(int_lists)
    co2_bit_array.compute_co2_scrubber_rating()
    co2_rating = co2_bit_array.decimal_co2_rating

    print(oxygen_rating * co2_rating)

part_two()

