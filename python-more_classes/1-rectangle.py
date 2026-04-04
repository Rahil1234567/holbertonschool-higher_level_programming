#!/usr/bin/python3
"""This script creates a rectangle class with methods and attributes."""


class Rectangle:
    """Rectangle class with attributes."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle object with private width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the private width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Raises:
        TypeError: if value is not an integer.
        ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Return the private height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Raises:
        TypeError: if value is not an integer.
        ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
