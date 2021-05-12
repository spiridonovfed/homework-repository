from typing import Generator

from homework4.task_5_optional import fizzbuzz


def test_positive_case1():
    """testing example from the task"""
    assert list(fizzbuzz(5)) == ["1", "2", "fizz", "4", "buzz"]


def test_positive_case2():
    assert list(fizzbuzz(16)) == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizzbuzz",
        "16",
    ]


def test_positive_case3():
    """checking that output is a generator"""
    assert isinstance(fizzbuzz("anything"), Generator)