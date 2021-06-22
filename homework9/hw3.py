"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """Function takes directory path, a file extension and an optional tokenizer.
    It will count lines in all files with that extension if there are no tokenizer.
    If a the tokenizer is not none, it will count tokens.

    :param dir_path: an instance of Path Class with path to directory needed
    :type dir_path: instance of Path class
    :param file_extension: file extension of files to count
    :type file_extension: str
    :param tokenizer: tokenizer function to split the data into tokens to count
    :type tokenizer: Callable, optional
    """

    # Get into directory
    cwd = os.getcwd()
    os.chdir(dir_path)
    files_to_work_with = os.listdir()

    # Count lines/tokens
    counter = 0
    for file in files_to_work_with:
        if not file.endswith(file_extension):
            continue
        file_content = open(file)
        for line in file_content:
            if tokenizer:
                counter += len(tokenizer.__call__(line))
            else:
                counter += 1

        file_content.close()

    # Change directory to previous state
    os.chdir(cwd)
    return counter
