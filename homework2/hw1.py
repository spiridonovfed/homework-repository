"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
from typing import List


def format_title(data):
    """formatting title: E R N S T -> ERNST"""
    pattern_title_letters = re.compile(r"[A-ZÄÖÜẞ]{1}([ ]{1}[A-ZÄÖÜẞ]{1})+")
    title_letters = pattern_title_letters.finditer(data)
    for match in title_letters:
        title_word = match.group()
        data = re.sub(title_word, title_word[::2], data)
    return data


def format_word_wraps(data):
    """Finding and replacing word wraps"""
    pattern_word_wraps = re.compile(r"\w+-\n\w+")
    word_wraps = pattern_word_wraps.finditer(data)
    for match in word_wraps:
        word_wrap = match.group()
        data = re.sub(
            word_wrap,
            "".join(letter for letter in word_wrap if letter.isalnum()) + "\n",
            data,
        )
    return data


def get_longest_diverse_words(file_path: str) -> List[str]:
    """ Finds 10 longest words consisting from largest amount of unique symbols """

    # opening and formatting the data:
    with open(file_path, encoding="unicode-escape") as file:
        data = file.read()
    data = format_title(data)
    data = format_word_wraps(data)

    # creating a list of all words in data:
    pattern_for_words = re.compile(r"\b\w+\b")
    words = pattern_for_words.finditer(data)
    words_list = [word.group() for word in words]

    # creating a dictionary [word1: quantity_of_unique_letters]
    words_dict = {}
    for word in words_list:
        unique_letters = []
        for letter in word:
            if not letter in unique_letters:
                unique_letters.append(letter)
        words_dict[word] = len(unique_letters)

    # sorting created dictionary by key and getting 10 longest diverse words
    longest_diverse_words = sorted(words_dict, key=words_dict.get, reverse=True)[:10]
    return longest_diverse_words


# print(get_longest_diverse_words("data.txt"))


def get_rarest_char(file_path: str) -> str:
    """Finds rarest symbol for document"""
    with open(file_path, encoding="unicode-escape") as file:
        data = file.read()
    # print(data)

    characters_dict = {}
    for char in data:
        if char in characters_dict.keys():
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    print(characters_dict)
    rarest_char = sorted(characters_dict, key=characters_dict.get, reverse=False)[0]
    # But there more than one symbol that have one time appearance in the text given
    return rarest_char


# print(get_rarest_char("data.txt"))


def count_punctuation_chars(file_path: str) -> int:
    """Counts every punctuation char"""
    with open(file_path, encoding="unicode-escape") as file:
        data = file.read()
    punctuation_pattern = re.compile(r"[^\w\s\d]")
    matches = punctuation_pattern.finditer(data)
    matches = tuple(matches)
    return len(matches)


# print(count_punctuation_chars("data.txt"))


def count_non_ascii_chars(file_path: str) -> int:
    """Counts every non ascii char"""
    with open(file_path, encoding="unicode-escape") as file:
        data = file.read()
    non_ascii_pattern = re.compile(r"[^\x00-\x7F]")
    matches = non_ascii_pattern.finditer(data)
    matches = tuple(matches)
    return len(matches)


# print(count_non_ascii_chars("data.txt"))


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Finds most common non ascii char for document"""
    with open(file_path, encoding="unicode-escape") as file:
        data = file.read()
    non_ascii_pattern = re.compile(r"[^\x00-\x7F]")
    matches = non_ascii_pattern.finditer(data)
    non_ascii_dict = {}
    for match in matches:
        ascii_char = match.group()
        if ascii_char not in non_ascii_dict.keys():
            non_ascii_dict[ascii_char] = 1
        else:
            non_ascii_dict[ascii_char] += 1
    most_common_nonascii_char = sorted(
        non_ascii_dict, key=non_ascii_dict.get, reverse=True
    )[0]
    return most_common_nonascii_char


# print(get_most_common_non_ascii_char("data.txt"))
