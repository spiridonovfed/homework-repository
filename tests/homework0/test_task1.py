import pytest

from homework0.task1 import some_function


@pytest.mark.skip(reason="homework is approved")
def test_some_function():
    assert some_function()
