from unittest import mock

import pytest

from homework4.task_2_mock_input import count_dots_on_i


@pytest.mark.skip(reason="homework is approved")
def test_example_from_task():
    assert count_dots_on_i("https://example.com/") == 59


with open("tests/homework4/Example Domain.html", "rb") as local_example_com:
    mock_data = local_example_com.read()


@pytest.mark.skip(reason="homework is approved")
@mock.patch("homework4.task_2_mock_input.open_url", return_value=mock_data)
def test_with_mocked_data(mock_read):
    assert count_dots_on_i("anything, because data is mocked") == 59


@pytest.mark.skip(reason="homework is approved")
def test_incorrect_URL():
    with pytest.raises(ValueError):
        count_dots_on_i("https://inNncCorrect.com/")
