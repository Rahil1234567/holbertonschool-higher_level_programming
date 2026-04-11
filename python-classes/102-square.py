#!/usr/bin/python3
"""Module that defines a Square class with comparison methods"""


class Square:
    """Represents a square for comparison"""

    def __init__(self, size=0):
        """Initialize the square"""
        self.size = size

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation (int or float)"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if areas are equal (==)"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if areas are not equal (!=)"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if area is less than (<)"""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if area is less than or equal (<=)"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if area is greater than (>)"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if area is greater than or equal (>=)"""
        return self.area() >= other.area()
