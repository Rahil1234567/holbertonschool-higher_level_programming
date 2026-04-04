#!/usr/bin/python3
"""Pickling and unpickling custom class with pickle module."""
import pickle


class CustomObject:
    """Custom class to pickle and unpickle."""

    def __init__(self, name, age, is_student):
        """Initialize object with instance attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance of object into file."""
        try:
            with open(filename, "wb") as file:
                return pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize pickled file into CustomObject instance."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
