from homework8.task2 import TableData

presidents = TableData("tests/homework8/example.sqlite", "presidents")
books = TableData("tests/homework8/example.sqlite", "books")


def test_len_function():
    assert len(presidents) == 3
    assert len(books) == 3


def test_getitem_function():
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert books["1984"] == ("1984", "Orwell")


def test_contains_function_positive_cases():
    assert "Trump" in presidents
    assert "1984" in books


def test_contains_function_negative_cases():
    assert not "Gagarin" in presidents
    assert not "Footbal" in books


def test_iteration_with_presidents(capsys):
    for president in presidents:
        print(president["name"])
    captured = capsys.readouterr()
    assert captured.out == "Yeltsin\nTrump\nBig Man Tyrone\n"


def test_iteration_with_books(capsys):
    for book in books:
        print(book["name"])
    captured = capsys.readouterr()
    assert captured.out == "Farenheit 451\nBrave New World\n1984\n"
