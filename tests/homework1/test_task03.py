import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.skip(reason="homework is approved")
def test_positive_case1():
    """Testing that function finds max and min number correctly"""
    assert find_maximum_and_minimum("tests/homework1/test_task03_data1.txt") == (
        -10,
        22,
    )


@pytest.mark.skip(reason="homework is approved")
def test_positive_case2():
    """Testing that function finds max and min number correctly"""
    assert find_maximum_and_minimum("tests/homework1/test_task03_data2.txt") == (
        -100,
        97,
    )


@pytest.mark.skip(reason="homework is approved")
def test_positive_case3():
    """Testing that function finds max and min number correctly"""
    assert find_maximum_and_minimum("tests/homework1/test_task03_data3.txt") == (
        -94,
        81,
    )
