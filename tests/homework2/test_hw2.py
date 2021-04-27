from homework2.hw2 import major_and_minor_elem


def test_positive_case1():
    """checking for Example 1 in the task"""
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_positive_case2():
    """checking for Example 2 in the task"""
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_positive_case3():
    """checking for'-' output for most common element, that appears less then n // 2 times"""
    assert major_and_minor_elem([1, 2, 2, 3, 3, 4, 4, 5, 5, 5]) == ("-", 1)


def test_negative_case1():
    """check if list of equal elements will give equal elements in output"""
    assert (
        not major_and_minor_elem([1, 1, 1, 1])[0]
        != major_and_minor_elem([1, 1, 1, 1])[1]
    )


def test_negative_case2():
    """check if list of 1 element passed will return a tuple with two that elements"""
    assert not major_and_minor_elem(["f"])[0] != major_and_minor_elem(["f"])[1]
