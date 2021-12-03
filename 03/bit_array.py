import numpy as np
import copy

class BitArray:
    def __init__(self, bits):
        self.bits = bits

        self.decimal_gamma = None
        self.binary_gamma = None

        self.decimal_epsilon = None
        self.binary_epsilon = None

        self.binary_oxygen_rating = None
        self.decimal_oxygen_rating = None

    def compute_gamma_rate(self):
        binary_gamma_str = ""
        binary_gamma_array = []

        np_arr = np.array(self.bits)
        rotated_array = np.rot90(np_arr, axes=(1,0))

        for bit_slice in rotated_array:
            _, counts = np.unique(bit_slice, return_counts=True)
            if len(counts) == 1 or counts[0] == counts[1]:
                most_frequent_bit = 1
            else:
                most_frequent_bit = np.bincount(bit_slice).argmax()

            binary_gamma_array.append(most_frequent_bit)
            binary_gamma_str += str(most_frequent_bit)

        decimal_gamma = int(binary_gamma_str, 2)
        self.decimal_gamma = decimal_gamma
        self.binary_gamma = binary_gamma_array


    def compute_epsilon_rate(self):
        if not self.binary_gamma:
            self.compute_gamma_rate()

        np_binary_gamma = np.array(self.binary_gamma)
        binary_epsilon = 1-np_binary_gamma
        str_binary_epsilon = [str(x) for x in binary_epsilon]
        str_binary_epsilon = "".join(str_binary_epsilon)

        self.binary_epsilon = binary_epsilon

        self.decimal_epsilon = int(str_binary_epsilon, 2)

    def compute_oxygen_generator_rating(self):
        if not self.binary_gamma:
            self.compute_gamma_rate()

        for idx, _ in enumerate(self.binary_gamma):
            bits_to_keep = copy.deepcopy(self.bits)
            for bits in self.bits:

                current_gamma = self.binary_gamma[idx]
                if current_gamma != bits[idx]:
                    bits_to_keep.remove(bits)


            self.bits = bits_to_keep
            self.compute_gamma_rate()

        self.binary_oxygen_rating = self.bits[0]
        str_binary_oxygen = [str(x) for x in self.binary_oxygen_rating]
        str_binary_oxygen = "".join(str_binary_oxygen)
        self.decimal_oxygen_rating = int(str_binary_oxygen, 2)


