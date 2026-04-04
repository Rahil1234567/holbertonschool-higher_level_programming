#!/usr/bin/python3
"""Script with a function to read file."""


def read_file(filename=""):
    """Read file and print the contents."""
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents, end="")
