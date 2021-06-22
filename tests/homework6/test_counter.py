from homework6.counter import User


def test_from_example1():
    assert User.get_created_instances() == 0


def test_from_example2():
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3
    assert user.get_created_instances() == 0


def test_for_class_passed_in_reset_counter():
    user, _, _ = User(), User(), User()
    assert User.reset_instances_counter() == 3
    assert user.get_created_instances() == 0
