import unittest
from submarine import Submarine

class TestSubmarineClass(unittest.TestCase):
    def test_init_submarine(self):
        new_submarine = Submarine();
        self.assertIsInstance(new_submarine, Submarine)

    def test_submarine_coordinates(self):
        new_submarine = Submarine();
        self.assertTrue(hasattr(new_submarine, "coordinates"))


