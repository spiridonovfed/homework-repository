import pytest

from homework1.task02 import check_fibonacci


@pytest.mark.skip(reason="homework is approved")
def test_positive_case1():
    """Testing that sequence given IS actually Fibonacci sequence(list given)"""
    assert check_fibonacci([2, 3, 5, 8, 13, 21, 34, 55])


@pytest.mark.skip(reason="homework is approved")
def test_positive_case2():
    """Testing that sequence given IS Fibonacci sequence(tuple given)"""
    assert check_fibonacci((144, 233, 377, 610, 987, 1597, 2584))


@pytest.mark.skip(reason="homework is approved")
def test_positive_case3():
    """Testing that sequence given IS Fibonacci sequence(tuple given)"""
    assert check_fibonacci((0, 1))


@pytest.mark.skip(reason="homework is approved")
def test_positive_case4():
    """Testing that sequence given IS Fibonacci sequence(list given)"""
    assert check_fibonacci((1, 1))


@pytest.mark.skip(reason="homework is approved")
def test_negative_case1():
    """Testing that sequence given IS NOT actually Fibonacci sequence(list given)"""
    assert not check_fibonacci([2, 4, 6, 10])


@pytest.mark.skip(reason="homework is approved")
def test_negative_case2():
    """Testing that sequence given IS NOT actually Fibonacci sequence(list given)"""
    assert not check_fibonacci([16, 5, 21, 26])


@pytest.mark.skip(reason="homework is approved")
def test_negative_case3():
    """Testing that sequence given IS NOT actually Fibonacci sequence(list given)"""
    assert not check_fibonacci([-14, -5, -19, -24])
