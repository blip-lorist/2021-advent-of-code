import unittest
from submarine import Submarine

class TestSubmarineClass(unittest.TestCase):
    def test_init_submarine(self):
        new_submarine = Submarine();
        self.assertIsInstance(new_submarine, Submarine)

    def test_submarine_coordinates(self):
        new_submarine = Submarine();
        self.assertTrue(hasattr(new_submarine, "coordinates"))
        self.assertTrue("horizontal" in new_submarine.coordinates)
        self.assertTrue("depth" in new_submarine.coordinates)

    def test_move_forward(self):
        new_submarine = Submarine();
        new_submarine.move("forward", 5)
        expected_coordinates = {"horizontal": 5, "depth": 0}
        actual_coordinates = new_submarine.coordinates
        self.assertEqual(expected_coordinates, actual_coordinates)

    def test_move_down(self):
        new_submarine = Submarine();
        new_submarine.move("down", 5)
        expected_coordinates = {"horizontal": 0, "depth": 5}
        actual_coordinates = new_submarine.coordinates
        self.assertEqual(expected_coordinates, actual_coordinates)

    def test_move_up(self):
        new_submarine = Submarine();
        new_submarine.move("up", 5)
        expected_coordinates = {"horizontal": 0, "depth": -5}
        actual_coordinates = new_submarine.coordinates
        self.assertEqual(expected_coordinates, actual_coordinates)

