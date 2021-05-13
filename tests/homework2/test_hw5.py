import string

import pytest

from homework2.hw5 import custom_range


@pytest.mark.skip(reason="homework is approved")
def test_positive_case1():
    """Testing example 1 from the task"""
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


@pytest.mark.skip(reason="homework is approved")
def test_positive_case2():
    """Testing example 2 from the task"""
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


@pytest.mark.skip(reason="homework is approved")
def test_positive_case3():
    """Testing example 3 from the task"""
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]


@pytest.mark.skip(reason="homework is approved")
def test_negative_case1():
    """Testing with string of non-ascii symbols"""
    assert not custom_range("äüöß", "ö") != ["ä", "ü"]


@pytest.mark.skip(reason="homework is approved")
def test_negative_case2():
    """Testing with lists"""
    assert not custom_range([1, 2, 3, 4, 5, 6], 2, 5) != [2, 3, 4]


@pytest.mark.skip(reason="homework is approved")
def test_negative_case3():
    """Testing with tuples"""
    assert not custom_range((1, 2, 3, 4, 5, 6), 2, 5) != [2, 3, 4]
