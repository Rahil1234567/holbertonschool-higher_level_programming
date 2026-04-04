#!/usr/bin/python3
"""Script to turn object into JSON representation."""
import json


def to_json_string(my_obj):
    """Turn the object into JSON representation."""
    return json.dumps(my_obj)
