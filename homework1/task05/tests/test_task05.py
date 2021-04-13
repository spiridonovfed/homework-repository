from task05 import find_maximal_subarray_sum


def test_positive_case1():
    """Testing that function finds subarray with max sum correctly"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], k=3) == 16


def test_positive_case2():
    """Testing that function finds subarray with max sum correctly"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], k=1) == 7


def test_positive_case3():
    """Testing that function finds subarray with max sum correctly"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], k=8) == 21
