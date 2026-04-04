#!/usr/bin/python3
"""Return dict description for JSON serialization of an object."""


def class_to_json(obj):
    """Return dictionary that stores the attributes of the object."""
    return obj.__dict__
