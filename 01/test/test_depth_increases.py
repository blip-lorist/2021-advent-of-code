import unittest
from depth_increases import count_increases

class TestFuelNeeded(unittest.TestCase):
    def test_count_increases(self):
        test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected_count = 7

        actual_count = count_increases(test_input)
        self.assertEqual(expected_count, actual_count)

