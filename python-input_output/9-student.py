#!/usr/bin/python3
"""Custom class and a function to return dictionary with attributes."""


class Student:
    """Custom Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize with first, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary that stores the attributes of the object."""
        return self.__dict__
