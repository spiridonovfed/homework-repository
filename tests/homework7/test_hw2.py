from homework7.hw2 import backspace_compare


def test_example_1():
    s = "ab#c"
    t = "ad#c"
    assert backspace_compare(s, t) is True


def test_example_2():
    s = "a##c"
    t = "#a#c"
    assert backspace_compare(s, t) is True


def test_example_3():
    a = "a#c"
    t = "b"
    assert backspace_compare(a, t) is False
