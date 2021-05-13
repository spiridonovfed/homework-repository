import pytest

from homework4.task_3_get_print_output import my_precious_logger


@pytest.mark.skip(reason="homework is approved")
def test_positive_case1(capsys):
    """Example 1 from the task"""
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"


@pytest.mark.skip(reason="homework is approved")
def test_positive_case2(capsys):
    """Example 2 from the task"""
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK"


@pytest.mark.skip(reason="homework is approved")
def test_positive_case3(capsys):
    my_precious_logger("NOT an error - captured in stdout")
    captured = capsys.readouterr()
    assert captured.out == "NOT an error - captured in stdout"


@pytest.mark.skip(reason="homework is approved")
def test_positive_case4(capsys):
    my_precious_logger("error - captured in stderr")
    captured = capsys.readouterr()
    assert captured.err == "error - captured in stderr"
