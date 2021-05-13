import pytest

from homework2.hw3 import combinations


@pytest.mark.skip(reason="homework is approved")
def test_positive_case1():
    """Testing example given"""
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


@pytest.mark.skip(reason="homework is approved")
def test_positive_case2():
    assert combinations([1], [2]) == [[1, 2]]


@pytest.mark.skip(reason="homework is approved")
def test_positive_case3():
    assert (
        len(
            combinations(
                ["A", "B", "C", "D", "E", "F", "G", "H"], [1, 2, 3, 4, 5, 6, 7, 8]
            )
        )
        == 64
    )


@pytest.mark.skip(reason="homework is approved")
def test_negative_case1():
    """checks that output is a list"""
    assert not type(combinations([1, 2], [3, 4])) != list


@pytest.mark.skip(reason="homework is approved")
def test_negative_case2():
    assert not combinations([1, 2], [3, 4]) == [
        [2, 4],
        [2, 3],
        [1, 4],
        [1, 3],
    ]
