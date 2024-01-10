#!/usr/bin/python3
"""Defines appending function in a text file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text (new_string) after given text (search_strin) in a file

    Args:
        filename (str): The file's name.
        search_string (str): The input string to search for.
        new_string (str): The text to append.
    """
    text = ""
    with open(filename) as r:
        for eachLine in r:
            text += eachLine
            if search_string in eachLine:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
