import unittest
from bit_array import BitArray

class TestBitArrayClass(unittest.TestCase):
    def test_init_bit_array(self):
        bits = [[0,0,0,0,0]]
        new_bit_array = BitArray(bits)
        self.assertIsInstance(new_bit_array, BitArray)

class TestComputeGammaRate(unittest.TestCase):
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

    expected_gamma_rate = 22
    actual_gamma_rate = new_bit_array.compute_gamma_rate
    self.assertEqual(expected_gamma_rate, actual_gamma_rate)
