#!/usr/bin/python3
"""Function to check if object is instance of the specified class or not."""


def inherits_from(obj, a_class):
    """Return True if the object is instance of class's super class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
