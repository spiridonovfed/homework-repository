from pathlib import Path

from homework9.hw3 import universal_file_counter

test_dir = Path("./")


def test_from_example_1():
    assert universal_file_counter(test_dir, "txt") == 6


def test_from_example_2():
    assert universal_file_counter(test_dir, "txt", str.split) == 6


test_subfolder = Path("./test_subfolder")


def test_count_lines():
    assert universal_file_counter(test_subfolder, "txt") == 10


def test_count_words():
    assert universal_file_counter(test_subfolder, "txt", str.split) == 27
