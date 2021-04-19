"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("test_data1.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    min_n = 0
    max_n = 0
    with open(file_name) as file:
        for line in file:
            number = int(line)
            if number < min_n:
                min_n = number
            if number > max_n:
                max_n = number
    return min_n, max_n
