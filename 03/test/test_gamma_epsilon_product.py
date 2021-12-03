import unittest
from bit_array import BitArray

class TestBitArrayClass(unittest.TestCase):
    def test_init_bit_array(self):
        bits = [[0,0,0,0,0]]
        new_bit_array = BitArray(bits)
        self.assertIsInstance(new_bit_array, BitArray)

class TestComputeGammaRate(unittest.TestCase):
    def test_compute_gamma_rate(self):
        bits = [[0, 0, 1, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 1, 1, 0],
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [0, 1, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [1, 1, 1, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0]]

        new_bit_array = BitArray(bits)

        expected_decimal_gamma = 22
        expected_binary_gamma = [1, 0, 1, 1, 0]

        new_bit_array.compute_gamma_rate()
        actual_decimal_gamma = new_bit_array.decimal_gamma
        actual_binary_gamma = new_bit_array.binary_gamma
        self.assertEqual(expected_decimal_gamma, actual_decimal_gamma)
        self.assertEqual(expected_binary_gamma, actual_binary_gamma)
