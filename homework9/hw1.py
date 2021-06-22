"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from typing import Iterator


def merge_sorted_files(file_list) -> Iterator:
    """
    Function merges integer from sorted files and returns an iterator

    file1.txt:
    1
    3
    5

    file2.txt:
    2
    4
    6

    >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
    [1, 2, 3, 4, 5, 6]
    """

    def generator():
        list_for_heapq = []
        for file in file_list:
            file_content = open(file)
            list_for_heapq.append(file_content)

        for line in heapq.merge(*list_for_heapq):
            yield int(line)

        for file in list_for_heapq:
            file.close()

    return iter(generator())
