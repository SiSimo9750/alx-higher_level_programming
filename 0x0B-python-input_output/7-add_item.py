#!/usr/bin/python3
"""Generate a Python list from arguments and save to a file."""


import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        generatedList = load_from_json_file("add_item.json")
    except FileNotFoundError:
        generatedList = []
    generatedList.extend(sys.argv[1:])
    save_to_json_file(generatedList, "add_item.json")
