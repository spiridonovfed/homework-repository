from task04 import check_sum_of_four


def test_positive_case1():
    """Testing that function finds number of tuples correctly"""
    assert check_sum_of_four([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2


def test_positive_case2():
    """Testing that function finds number of tuples correctly"""
    assert (
        check_sum_of_four(
            [-12, 55, 11, 4, 10], [8, 3], [-10, 7, 33], [19, 41, 37, -40, -3]
        )
        == 4
    )
