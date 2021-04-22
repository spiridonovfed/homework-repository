from unittest import mock

from homework4.task_2_mock_input import count_dots_on_i


def test_example_from_task():
    assert count_dots_on_i("https://example.com/") == 59


with open("tests/homework4/Example Domain.html", "rb") as local_example_com:
    mock_data = local_example_com.read()


@mock.patch("homework4.task_2_mock_input.open_url", return_value=mock_data)
def test_with_mocked_data(mock_read):
    assert count_dots_on_i("anything, because data is mocked") == 59


def test_incorrect_URL():
    with pytest.raises(ValueError):
        count_dots_on_i("https://inNncCorrect.com/")
