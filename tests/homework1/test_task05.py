import pytest

from homework1.task05 import find_maximal_subarray_sum


@pytest.mark.skip(reason="homework is approved")
def test_positive_case1():
    """Testing that function finds subarray with max sum correctly"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], k=3) == 16


@pytest.mark.skip(reason="homework is approved")
def test_positive_case2():
    """Testing that function finds subarray with max sum correctly"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], k=1) == 7


@pytest.mark.skip(reason="homework is approved")
def test_positive_case3():
    """Testing that function finds subarray with max sum correctly"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], k=8) == 21


@pytest.mark.skip(reason="homework is approved")
def test_negative_case1():
    """Testing with k > len(num)"""
    assert not find_maximal_subarray_sum([1, 2, 3], k=4)


@pytest.mark.skip(reason="homework is approved")
def test_negative_case2():
    """Check for output data type"""
    assert not type(find_maximal_subarray_sum([1, 2, 3], k=1)) != int


@pytest.mark.skip(reason="homework is approved")
def test_negative_case3():
    """Testing with k=0"""
    assert not find_maximal_subarray_sum([1, 2, 3], k=0) != 0
