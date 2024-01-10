#!/usr/bin/python3
"""Defines a JSON file reading function."""
import json

def load_from_json_file(filename):
    """Will creat an object from a JSON file source."""
    with open(filename) as f:
        return json.load(f)
