"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from math import sqrt
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """ Checking if sequence given is a fibonacci sequence """

    # checking if the first number in sequence is fibonacci number -
    # function returns "False" if it's not:
    if not data[0] == 0:
        if not (
            sqrt(5 * (data[0] ** 2) - 4) % 1 == 0
            or sqrt(5 * (data[0] ** 2) + 4) % 1 == 0
        ):
            return False

    # checking if the second number in sequence is fibonacci number -
    # function returns "False" if it's not:
    if not (
        sqrt(5 * (data[1] ** 2) - 4) % 1 == 0 or sqrt(5 * (data[1] ** 2) + 4) % 1 == 0
    ):
        return False

    # checking if a sequence given is fibonacci sequence
    index = 0
    while index < len(data) - 2:
        if data[index] + data[index + 1] == data[index + 2]:
            index += 1
        else:
            return False

    return True
