import pytest

from homework5.oop_1 import Homework, Student, Teacher

# ---------------------------------------------#

teacher = Teacher("Daniil", "Shadrin")
student = Student("Roman", "Petrov")


@pytest.mark.skip(reason="homework is approved")
def test_from_example1():
    assert teacher.last_name == "Shadrin"


@pytest.mark.skip(reason="homework is approved")
def test_from_example2():
    assert student.first_name == "Roman"


# ---------------------------------------------#

expired_homework = teacher.create_homework("Learn functions", 0)


@pytest.mark.skip(reason="homework is approved")
def test_from_example3():
    assert str(expired_homework.deadline) == "0:00:00"


@pytest.mark.skip(reason="homework is approved")
def test_from_example4():
    assert expired_homework.text == "Learn functions"


# ---------------------------------------------#
# create function from method and use it
create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 5)


@pytest.mark.skip(reason="homework is approved")
def test_from_example5():
    assert str(oop_homework.deadline) == "5 days, 0:00:00"


# ---------------------------------------------#


@pytest.mark.skip(reason="homework is approved")
def test_from_example6(capsys):
    assert student.do_homework(expired_homework) == None
    captured = capsys.readouterr()
    assert captured.out == "You are late\n"
