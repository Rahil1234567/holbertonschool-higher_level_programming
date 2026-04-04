#!/usr/bin/python3
"""Script to turn JSON string into Python data structure (object)."""
import json


def from_json_string(my_str):
    """Turn JSON string into python object."""
    return json.loads(my_str)
