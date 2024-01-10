#!/usr/bin/python3
"""Generate list from arguments and save to a file."""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    extractedList = load_from_json_file("add_item.json")
except FileNotFoundError:
    extractedList = []
extractedList.extend(sys.argv[1:])
save_to_json_file(extractedList, "add_item.json")
