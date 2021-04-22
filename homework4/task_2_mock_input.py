"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


# >>> count_dots_on_i("https://example.com/")
# 59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import urllib.request
from urllib.error import URLError


def open_url(url):
    """separate function to read data from site in order to be able to mock it"""
    try:
        data = urllib.request.urlopen(url).read()
        return data
    except URLError:
        raise ValueError(f"Unreachable {url}")


def count_dots_on_i(url: str) -> int:
    """
    Counts how many letters `i` are present in the HTML by this URL
    >>> count_dots_on_i("https://example.com/")
    59
    >>> count_dots_on_i("https://ru.simplesite.com/default.aspx")
    1830
    """
    data = open_url(url)
    str_data = str(data)
    i_count = str_data.count("i")
    return i_count
