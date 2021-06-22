from homework9.hw2 import Suppressor, suppressor


# -- test a context manager as a class: -- #
def test_example_from_task():
    with Suppressor(IndexError):
        [][2]


def test_with_ZeroDivisionError():
    with Suppressor(ZeroDivisionError):
        result = 11 / 0


def test_with_NameError():
    with Suppressor(NameError):
        result = name + 14


# -- test a context manager as a function: -- #
def test_example_from_task_():
    with suppressor(IndexError):
        result = [][2]


def test_with_ZeroDivisionError_():
    with suppressor(ZeroDivisionError):
        result = 11 / 0


def test_with_NameError_():
    with suppressor(NameError):
        result = name + 14
