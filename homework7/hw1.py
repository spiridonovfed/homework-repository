"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

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


#######################################################
def find_occurrences(tree: dict, element: Any) -> int:
    def iteritems(d, **kw):
        """Returns iterator of dictionary's items"""
        return iter(d.items(**kw))

    def recursion(dictionary, item):
        """Recursively searches for item and increments counter"""
        nonlocal counter

        if dictionary.get(item) is not None:
            counter += 1
        elif item in list(dictionary.values()):
            counter += list(dictionary.values()).count(item)

        for key, value in iteritems(dictionary):
            if isinstance(value, dict):
                recursion(value, item)
            elif isinstance(value, list):
                for list_item in value:
                    if hasattr(list_item, "items"):
                        recursion(list_item, item)
                    elif list_item == item:
                        counter += 1

    counter = 0
    # Applying recursive search to tree passed in
    recursion(tree, element)

    return counter


# if __name__ == "__main__":
#     print(find_occurrences(example_tree, "RED"))  # 6
