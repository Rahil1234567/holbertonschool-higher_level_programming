#!/usr/bin/python3
"""This script creates a class Square."""


class Square:
    """Define a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Raise:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the square's area."""
        return self.__size ** 2
