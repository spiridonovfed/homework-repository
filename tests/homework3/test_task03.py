import pytest

from homework3.task03 import Filter, make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


@pytest.mark.skip(reason="homework is approved")
def test_case1():
    """checks if 'functions attribute is a tuple'"""
    filter = Filter()
    assert type(filter.functions) == tuple


@pytest.mark.skip(reason="homework is approved")
def test_case2():
    """checks with a filter for long words in list of words"""
    sentence = [
        "Lists",
        "and",
        "tuples",
        "are",
        "sequence",
        "data",
        "structures",
        "that",
        "can",
        "contain",
        "objects",
        "of",
        "different",
        "data",
        "types",
    ]
    long_words = Filter(lambda a: isinstance(a, str), lambda a: len(a) > 7)
    assert long_words.apply(sentence) == ["sequence", "structures", "different"]


@pytest.mark.skip(reason="homework is approved")
def test_case3():
    """testing the example from task"""
    assert make_filter(name="polly", type="bird").apply(sample_data) == [sample_data[1]]


@pytest.mark.skip(reason="homework is approved")
def test_case4():
    """if no filters applied - returns sample data"""
    assert make_filter().apply(sample_data) == sample_data


@pytest.mark.skip(reason="homework is approved")
def test_case5():
    """case where there's no match in data"""
    assert make_filter(type="person", name="NONAME").apply(sample_data) == []
