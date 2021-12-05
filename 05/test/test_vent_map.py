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
        self.assertTrue(hasattr(vent_map, "render"))

