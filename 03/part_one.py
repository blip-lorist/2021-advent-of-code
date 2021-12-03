import sys
import os.path
from bit_array import BitArray

def part_one():
    with open("puzzle_input", "r") as input_file:
        string_list = input_file.readlines()

    int_lists = []
    for bits in string_list:
        bits_int_list = [int(x) for x in bits.strip()]
        int_lists.append(bits_int_list)

    new_bit_array = BitArray(int_lists)
    new_bit_array.compute_gamma_rate()
    new_bit_array.compute_epsilon_rate()
    print(new_bit_array.decimal_gamma * new_bit_array.decimal_epsilon)

part_one()

