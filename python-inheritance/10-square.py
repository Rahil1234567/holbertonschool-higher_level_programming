#!/usr/bin/python3
"""Script with Geometry class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherited from Rectangle class."""

    def __init__(self, size):
        """Initialize square with size and validate it."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return square area."""
        return self.__size ** 2
