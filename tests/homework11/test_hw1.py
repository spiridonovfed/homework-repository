import pytest

from homework11.hw1 import SimplifiedEnum


@pytest.fixture()
def ColorsEnum():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    return ColorsEnum


@pytest.fixture()
def SizesEnum():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    return SizesEnum


def test_from_example_1(ColorsEnum):
    assert ColorsEnum.RED == "RED"


def test_from_example_2(SizesEnum):
    assert SizesEnum.XL == "XL"


def test_positive_case(ColorsEnum):
    assert ColorsEnum.BLACK == "BLACK"


def test_non_existing_key(SizesEnum):
    with pytest.raises(KeyError):
        SizesEnum.XYZL
