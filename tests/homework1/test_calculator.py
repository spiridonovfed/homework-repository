from homework1.sample_project_calc import check_power_of_2


def test_positive_case1():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_positive_case2():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(16384)


def test_positive_case3():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(4096)


def test_negative_case1():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(25)


def test_negative_case2():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(49)
