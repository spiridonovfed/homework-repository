from homework3.task04 import is_armstrong


def test_positive_case1():
    assert is_armstrong(9)


def test_negative_case1():
    assert not is_armstrong(19)


def test_positive_case2():
    assert is_armstrong(153)


def test_negative_case2():
    assert not is_armstrong(11)


def test_positive_case3():
    assert is_armstrong(407)


def test_negative_case3():
    assert not is_armstrong(400)


def test_case_with_negative_number():
    assert not is_armstrong(-44)
