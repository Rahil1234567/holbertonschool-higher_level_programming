#!/usr/bin/python3
"""Script with a function to manipulate files."""


def append_write(filename="", text=""):
    """Append the string to the file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
