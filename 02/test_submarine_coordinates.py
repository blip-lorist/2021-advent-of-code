import unittest
from submarine import Submarine

class TestPartOne(unittest.TestCase):
    def test_init_submarine(self):
        new_submarine = Submarine();
        self.assertIsInstance(new_submarine, Submarine)
