import unittest
from submarine import Submarine

class TestSubmarineClass(unittest.TestCase):
    def test_init_submarine(self):
        new_submarine = Submarine();
        self.assertIsInstance(new_submarine, Submarine)

    def test_submarine_coordinates(self):
        new_submarine = Submarine();
        self.assertTrue(hasattr(new_submarine, "coordinates"))
        self.assertTrue(hasattr(new_submarine, "aim"))
        self.assertTrue(hasattr(new_submarine, "use_aim"))
        self.assertTrue("horizontal" in new_submarine.coordinates)
        self.assertTrue("depth" in new_submarine.coordinates)


class TestMovement(unittest.TestCase):
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

class TestMovementWithAim(unittest.TestCase):
    def test_move_down(self):
        new_submarine = Submarine(use_aim=True);
        new_submarine.move("down", 5)
        expected_coordinates = {"horizontal": 0, "depth": 0}
        expected_aim = 5

        actual_coordinates = new_submarine.coordinates
        actual_aim = new_submarine.aim
        self.assertEqual(expected_coordinates, actual_coordinates)
        self.assertEqual(expected_aim, actual_aim)

    def test_move_forward_with_aim(self):
        new_submarine = Submarine(use_aim=True);
        new_submarine.move("down", 5)
        new_submarine.move("forward", 8)
        expected_coordinates = {"horizontal": 8, "depth": 40}
        expected_aim = 5

        actual_coordinates = new_submarine.coordinates
        actual_aim = new_submarine.aim
        self.assertEqual(expected_coordinates, actual_coordinates)
        self.assertEqual(expected_aim, actual_aim)

    def test_move_up(self):
        new_submarine = Submarine(use_aim=True);
        new_submarine.move("up", 3)
        expected_coordinates = {"horizontal": 0, "depth": 0}
        expected_aim = -3

        actual_coordinates = new_submarine.coordinates
        actual_aim = new_submarine.aim
        self.assertEqual(expected_coordinates, actual_coordinates)
        self.assertEqual(expected_aim, actual_aim)

class TestPartOne(unittest.TestCase):
    def test_(self):
        new_submarine = Submarine();
        movements = [
            ("forward", 5),
            ("down", 5),
            ("forward", 8),
            ("up", 3),
            ("down", 8),
            ("forward", 2),
        ]

        for movement in movements:
            direction, distance  = movement
            new_submarine.move(direction, distance)

        expected_coordinates = {"horizontal": 15, "depth": 10}
        actual_coordinates = new_submarine.coordinates

        self.assertEqual(expected_coordinates, actual_coordinates)

