from homework8.task1 import KeyValueStorage

storage = KeyValueStorage("tests/homework8/test_task1.txt")


def test_example_1_from_task():
    assert storage.name == "kek"


def test_example_2_from_task():
    assert storage.song == "shadilay"


def test_example_3_from_task():
    assert storage.power == 9001
    assert isinstance(storage.power, int)


def test_recognize_float():
    assert isinstance(storage.float_number, float)


def test_does_not_ovewrite_built_ins():
    assert storage.__dict__ != "will_not_overwrite_built-in_method"


def test_assign_attr_with_double_underscore():
    assert storage.__secret == "UFO_exist"
