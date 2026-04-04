#!/usr/bin/python3
"""This script creates a rectangle class with methods and attributes."""


class Rectangle:
    """Rectangle class with attributes."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle object with private width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Return rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of rectangle, 0 if height or width is 0."""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string of # s in the size of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            lines = ["#" * self.__width for _ in range(self.__height)]
            return "\n".join(lines)

    def __repr__(self):
        """Return the string expression Rectangle(width, height)."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Display message after deleting the object."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare rect_1 and rect_2 and return the one with bigger area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a rectangle object with size=height=width."""
        return cls(size, size)
