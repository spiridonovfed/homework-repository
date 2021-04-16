from homework1.task04 import check_sum_of_four


def test_positive_case1():
    """Testing that function finds number of tuples correctly"""
    assert check_sum_of_four([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2


def test_positive_case2():
    """Testing that function finds number of tuples correctly"""
    assert (
        check_sum_of_four(
            [-12, 55, 11, 4, 10],
            [8, 3, 5, 11, 10],
            [-10, 7, 33, -14, 8],
            [19, 41, 37, -40, -3],
        )
        == 4
    )


def test_positive_case3():
    """Testing that function finds number of tuples correctly"""
    assert check_sum_of_four([-4, -3, -2], [-1, 0, 1], [2, 3, 4], [5, -1, 7]) == 6


def test_negative_case1():
    """Testing that function finds number of tuples incorrectly"""
    a = [integer for integer in range(100)]
    b = [-integer for integer in range(100)]
    assert not check_sum_of_four(a, b, a, b) == 1


def test_negative_case2():
    """Testing that function finds number of tuples incorrectly"""
    a = [integer for integer in range(1000)]
    b = [-integer for integer in range(1000)]
    assert not check_sum_of_four(a, b, a, b) != 666667000


def test_negative_case3():
    """Testing that function finds number of tuples incorrectly"""
    assert not check_sum_of_four([0, 0], [0, 0], [0, 0], [0, 0]) != 2 ** 4
