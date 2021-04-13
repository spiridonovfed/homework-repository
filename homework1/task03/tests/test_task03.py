from task03 import find_maximum_and_minimum


def test_positive_case1():
    """Testing that function finds max and min number correctly"""
    assert find_maximum_and_minimum("tests/test_data1.txt") == (-10, 22)


def test_positive_case2():
    """Testing that function finds max and min number correctly"""
    assert find_maximum_and_minimum("tests/test_data2.txt") == (-100, 97)


def test_positive_case3():
    """Testing that function finds max and min number correctly"""
    assert find_maximum_and_minimum("tests/test_data3.txt") == (-94, 81)
