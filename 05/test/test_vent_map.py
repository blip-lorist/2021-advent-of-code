import unittest
from vents import VentMap


class TestVentMap(unittest.TestCase):

    def setUp(self):
        self.lines = [
            (0,9), (5,9),
            (8,0), (0,8),
            (9,4), (3,4),
            (2,2), (2,1),
            (7,0), (7,4),
            (6,4), (2,0),
            (0,9), (2,9),
            (3,4), (1,4),
            (0,0), (8,8),
            (5,5), (8,2)
        ]

    def test_init_vent_map(self):
        vent_map = VentMap(self.lines)
        self.assertTrue(hasattr(vent_map, "lines"))
        self.assertTrue(hasattr(vent_map, "covered_points"))

    def test_generate_covered_points(self):
        vent_map = VentMap(self.lines)
        vent_map.generate_covered_points()

        expected_points = [
                (7, 0),
                (7, 1),
                (7, 2),
                (7, 3),
                (2, 1),
                (2, 2),
                (1, 4),
                (2, 4),
                (3, 4),
                (3, 4),
                (4, 4),
                (5, 4),
                (6, 4),
                (7, 4),
                (7, 4),
                (8, 4),
                (9, 4),
        ]

        self.assertEqual(expected_points, vent_map.covered_points)

