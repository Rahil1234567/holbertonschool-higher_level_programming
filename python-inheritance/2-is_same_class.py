#!/usr/bin/python3
"""Function to check if object is instance of the specified class or not."""


def is_same_class(obj, a_class):
    """Return True if the object is exactly instance of spesified class."""
    return type(obj) is a_class
