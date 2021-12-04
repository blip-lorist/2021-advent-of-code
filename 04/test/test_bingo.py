import unittest
from bingo import BingoBoard


class TestBingo(unittest.TestCase):

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
        self.assertTrue(hasattr(board, "last_number_checked"))
        self.assertEqual(self.board_values, board.values)

    def test_mark_tile(self):
        board = BingoBoard(self.board_values)
        board.mark_tile(7)

        expected_coordinates = [(4, 4)]
        actual_coordinates = board.marked_coordinates
        self.assertEqual(expected_coordinates, actual_coordinates)

    def test_has_win(self):
        board = BingoBoard(self.board_values)
        board.mark_tile(7)

        expected_win_state = False
        actual_win_state = board.has_win()
        self.assertEqual(expected_win_state, actual_win_state)

        board.mark_tile(14)
        board.mark_tile(21)
        board.mark_tile(17)
        board.mark_tile(4)
        board.mark_tile(24)

        expected_win_state = True
        actual_win_state = board.has_win()
        self.assertEqual(expected_win_state, actual_win_state)

    def test_compute_final_score(self):
        board = BingoBoard(self.board_values)
        board.mark_tile(14)
        board.mark_tile(21)
        board.mark_tile(17)
        board.mark_tile(4)
        board.mark_tile(24)

        expected_final_score = 4512
        actual_final_score = compute_final_score()
