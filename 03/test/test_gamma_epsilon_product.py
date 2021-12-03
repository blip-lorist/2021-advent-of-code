import unittest
from bit_array import BitArray

class TestSubmarineClass(unittest.TestCase):
    def test_init_bit_array(self):
        bits = [[0,0,0,0,0]]
        new_bit_array = BitArray(bits)
        self.assertIsInstance(new_bit_array, BitArray)
