#!/usr/bin/python3
"""Script with a function to manipulate files."""


def write_file(filename="", text=""):
    """Add the string to file, return the number of characters added."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
