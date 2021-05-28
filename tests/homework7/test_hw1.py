from homework7.hw1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def test_the_example_given():
    assert find_occurrences(example_tree, "RED") == 6


def test_positive_case1():
    assert find_occurrences(example_tree, "of") == 2


def test_for_absent_value():
    assert find_occurrences(example_tree, "absent value") == 0
