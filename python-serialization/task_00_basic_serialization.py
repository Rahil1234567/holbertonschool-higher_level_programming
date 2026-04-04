#!/usr/bin/python3
"""Serialize and Deserialize JSON File."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save the python object as json data."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """Deserialize json file into python object."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
