#!/usr/bin/python3
"""Defines a file appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file with UTF8 coding.

    Args:
        filename (str): Destination file name.
        text (str): The input string to append.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
