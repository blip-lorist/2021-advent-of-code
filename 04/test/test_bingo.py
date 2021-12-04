import unittest
from bingo import BingoBoard


class TestBitArrayClass(unittest.TestCase):

    def setUp(self):
        self.board_values = [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6,  5],
            [2,  0,  12, 3,  7],
        ]

    def test_init_bingo_board(self):
        board = BingoBoard(self.board_values)
        self.assertTrue(hasattr(board, "values"))
        self.assertEqual(self.board_values, board.values)

