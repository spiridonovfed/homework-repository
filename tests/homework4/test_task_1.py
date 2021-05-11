import pytest

from homework4.task_1_read_file import read_magic_number


def test_positive_case1(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "data.txt"

    p.write_text("1")
    assert read_magic_number(p) == True


def test_positive_case2(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "data.txt"

    p.write_text("2.99")
    assert read_magic_number(p) == True


def test_positive_case3(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "data.txt"

    p.write_text("3")
    assert read_magic_number(p) == False


def test_positive_case4(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "data.txt"

    p.write_text("0")
    assert read_magic_number(p) == False


def test_positive_case5(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "data.txt"

    p.write_text("4")
    assert read_magic_number(p) == False


def test_negative_case1(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "data.txt"

    p.write_text("2\n" "0\n\\" "abrakadabra")
    assert read_magic_number(p) == True


def test_negative_case2(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "data.txt"

    p.write_text("12\n" "0\n\\" "abrakadabra")
    assert read_magic_number(p) == False


def test_negative_case3(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "data.txt"

    p.write_text("abrakadabra")
    assert pytest.raises(ValueError)


def test_negative_case4(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "data.txt"

    p.write_text("abrakadabra\n" "4\n" "11")
    assert pytest.raises(ValueError)
