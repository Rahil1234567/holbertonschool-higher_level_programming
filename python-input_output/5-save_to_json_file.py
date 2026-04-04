#!/usr/bin/python3
"""Script to write an object to a text file, using a JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Write python object as json string to file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
