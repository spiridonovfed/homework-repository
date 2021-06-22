from homework7.hw3 import tic_tac_toe_checker


def test_from_example_1():
    unfinished_board = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]

    assert tic_tac_toe_checker(unfinished_board) == "unfinished!"


def test_from_example_2():
    board = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_x_wins():
    board = [["-", "x", "o"], ["-", "x", "x"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_o_wins():
    board = [["-", "x", "o"], ["-", "o", "o"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_nobody_wins_and_unfinished():
    board = [["-", "x", "o"], ["-", "o", "x"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(board) == "unfinished!"


def test_draw():
    board = [["x", "x", "o"], ["o", "o", "x"], ["x", "x", "o"]]
    assert tic_tac_toe_checker(board) == "draw!"
