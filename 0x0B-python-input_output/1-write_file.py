#!/usr/bin/python3
"""Defines a file writing function."""


def write_file(filename="", text=""):
    """Write a string to a text file with UTF8 coding.

    Args:
        filename (str): Tfile's name to creat.
        text (str): The input text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
