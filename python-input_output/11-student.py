#!/usr/bin/python3
"""Custom class and a function to return dictionary with attributes."""


class Student:
    """Custom Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize with first, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary that stores the attributes of the object."""
        if isinstance(attrs, list) and \
                all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
