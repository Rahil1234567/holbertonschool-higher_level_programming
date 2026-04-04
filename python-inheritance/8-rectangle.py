#!/usr/bin/python3
"""Script with Geometry class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherited from BaseGeometry class."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height and validate both."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
