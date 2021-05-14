"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from collections import Counter
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    def get_horizontal_and_vertical_indexes(any_board):
        """returns a list of horizontal and vertical lines cells' indexes"""
        horizontal_lines_indexes = []
        vertical_lines_indexes = []
        for index_1, sublist in enumerate(any_board):
            horizontal_line_indexes = []
            vertical_line_indexes = []
            for index_2, symbol in enumerate(sublist):
                horizontal_line_indexes.append((index_1, index_2))
                vertical_line_indexes.append((index_2, index_1))
            horizontal_lines_indexes.append(horizontal_line_indexes)
            vertical_lines_indexes.append(vertical_line_indexes)

        return horizontal_lines_indexes + vertical_lines_indexes

    def get_diagonal_indexes(any_board):
        """returns a list of diagonal lines cells' indexes"""
        diagonal_line_1_indexes = []
        for index, sublist in enumerate(any_board):
            diagonal_line_1_indexes.append((index, index))
        diagonal_line_2_indexes = []
        for index, sublist in enumerate(any_board):
            diagonal_line_2_indexes.append((index, len(sublist) - index - 1))

        return [diagonal_line_1_indexes] + [diagonal_line_2_indexes]

    all_lines_indexes = get_horizontal_and_vertical_indexes(
        board
    ) + get_diagonal_indexes(board)

    empty_spot = False
    for line in all_lines_indexes:
        counter = Counter()
        for symbol in [board[cell[0]][cell[1]] for cell in line]:
            counter[symbol] += 1

        if counter["x"] == 3:
            return "x wins!"
        if counter["o"] == 3:
            return "o wins!"

        if counter["-"]:
            empty_spot = True

    if empty_spot:
        return "unfinished!"

    else:
        return "draw!"
