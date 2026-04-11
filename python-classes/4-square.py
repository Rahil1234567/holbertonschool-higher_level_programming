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

    @property
    def size(self):
        """Return the private size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Raises:
        TypeError: if value is not an integer.
        ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Print the square with # s."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
