#!/usr/bin/python3
"""Creating a function that adds attribute to class if it's possible."""


def add_attribute(obj, attr_name, value):
    """Add an attribute and value to object if possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
