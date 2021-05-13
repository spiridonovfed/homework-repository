import pytest

from homework3.task04 import is_armstrong


@pytest.mark.skip(reason="homework is approved")
def test_positive_case1():
    assert is_armstrong(9)


@pytest.mark.skip(reason="homework is approved")
def test_negative_case1():
    assert not is_armstrong(19)


@pytest.mark.skip(reason="homework is approved")
def test_positive_case2():
    assert is_armstrong(153)


@pytest.mark.skip(reason="homework is approved")
def test_negative_case2():
    assert not is_armstrong(11)


@pytest.mark.skip(reason="homework is approved")
def test_positive_case3():
    assert is_armstrong(407)


@pytest.mark.skip(reason="homework is approved")
def test_negative_case3():
    assert not is_armstrong(400)


@pytest.mark.skip(reason="homework is approved")
def test_case_with_negative_number():
    assert not is_armstrong(-44)
