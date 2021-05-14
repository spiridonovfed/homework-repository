"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Using nested-lookup package (https://pypi.org/project/nested-lookup/)
from nested_lookup import get_occurrence_of_value

# Example tree:
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

# Option 1
def find_occurrences(tree: dict, element: Any) -> int:
    return get_occurrence_of_value(tree, element)

# # Option 2
# def find_occurrences(tree: dict, element: Any) -> int:
#     return str(tree).count(str(element))


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
