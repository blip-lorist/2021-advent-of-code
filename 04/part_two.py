import sys
import os.path
from bingo import BingoBoard

def part_two():
    with open("puzzle_input", "r") as input_file:
        string_list = input_file.readlines()

    last_winning_board = None
    called_numbers = string_list.pop(0)
    string_list.pop(0)
    called_numbers_list = called_numbers.split(",")
    called_numbers_list = [int(x) for x in called_numbers_list]

    bingo_values = [string_list[x:x+6] for x in range(0, len(string_list), 6) ]

    board_list = []
    for board in bingo_values:
        try:
            board.pop(5)
        except:
            print("")

        scrubbed_board = []
        for row in board:
            row_list = row.split()
            row_list = [int(x) for x in row_list]
            scrubbed_board.append(row_list)

        new_board = BingoBoard(scrubbed_board)
        board_list.append(new_board)

    for called_number in called_numbers_list:
        for game_board in board_list:

            if not game_board.won:
                game_board.mark_tile(called_number)
                if game_board.has_win():
                    last_winning_board = game_board

    print(last_winning_board.compute_final_score())


part_two()

