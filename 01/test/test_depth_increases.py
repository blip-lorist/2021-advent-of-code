import unittest
from depth_increases import count_increases, window_sums_list

class TestFuelNeeded(unittest.TestCase):
    def test_count_increases(self):
        test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected_count = 7

        actual_count = count_increases(test_input)
        self.assertEqual(expected_count, actual_count)


    def test_window_sums(self):
        test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected_sums = [607, 618, 618, 617, 647, 716, 769, 792]

        actual_sums = window_sums_list(test_input)

        self.assertEqual(expected_sums, actual_sums)

