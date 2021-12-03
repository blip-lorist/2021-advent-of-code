import numpy as np

class BitArray:
    def __init__(self, bits):
        self.bits = np.array(bits)
        self.decimal_gamma = None

    def compute_gamma_rate(self):
        binary_gamma_str = ""
        rotated_array = np.rot90(self.bits, axes=(1,0))
        for bit_slice in rotated_array:
            most_frequent_bit = np.bincount(bit_slice).argmax()
            binary_gamma_str += str(most_frequent_bit)

        decimal_gamma = int(binary_gamma_str, 2)
        self.gamma_rate = decimal_gamma



