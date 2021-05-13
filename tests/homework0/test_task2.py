import pytest

from homework0.task2 import another_function


@pytest.mark.skip(reason="homework is approved")
def test_another_function():
    assert another_function() == "OK"
