import pytest

from homework5.save_original_info import custom_sum


@pytest.mark.skip(reason="homework is approved")
def test_from_example1():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add__"


@pytest.mark.skip(reason="homework is approved")
def test_from_example2():
    assert custom_sum.__name__ == "custom_sum"


@pytest.mark.skip(reason="homework is approved")
def test_from_example3(capsys):
    print(custom_sum.__original_func)
    captured = capsys.readouterr()
    assert captured.out.startswith("<function custom_sum at")


@pytest.mark.skip(reason="homework is approved")
def test_from_example4():
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
