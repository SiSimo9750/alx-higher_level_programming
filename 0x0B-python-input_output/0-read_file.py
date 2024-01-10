#!/usr/bin/python3
"""Defines a file reading function"""


def read_file(filename=""):
    """Print the text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
