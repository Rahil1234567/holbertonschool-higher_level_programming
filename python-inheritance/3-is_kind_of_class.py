#!/usr/bin/python3
"""Function to check if object is instance of the specified class or not."""


def is_kind_of_class(obj, a_class):
    """Return True if the object is instance of spesified or super class."""
    return isinstance(obj, a_class)
