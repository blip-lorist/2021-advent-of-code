import numpy as np

class BitArray:
    def __init__(self, bits):
        self.bits = np.array(bits)
        self.decimal_gamma = None
        self.binary_gamma = None

    def compute_gamma_rate(self):
        binary_gamma_str = ""
        binary_gamma_array = []

        rotated_array = np.rot90(self.bits, axes=(1,0))

        for bit_slice in rotated_array:
            most_frequent_bit = np.bincount(bit_slice).argmax()
            binary_gamma_array.append(most_frequent_bit)
            binary_gamma_str += str(most_frequent_bit)

        decimal_gamma = int(binary_gamma_str, 2)
        self.decimal_gamma = decimal_gamma
        self.binary_gamma = binary_gamma_array



