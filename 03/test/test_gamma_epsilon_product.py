import unittest
from bit_array import BitArray
import numpy as np


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

    def test_compute_epsilon_rate(self):
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

        expected_decimal_epsilon = 9
        expected_binary_epsilon = np.array([0, 1, 0, 0, 1])

        new_bit_array.compute_epsilon_rate()
        actual_decimal_epsilon = new_bit_array.decimal_epsilon
        actual_binary_epsilon = new_bit_array.binary_epsilon

        self.assertEqual(expected_decimal_epsilon, actual_decimal_epsilon)
        np.testing.assert_array_equal(expected_binary_epsilon, actual_binary_epsilon)
