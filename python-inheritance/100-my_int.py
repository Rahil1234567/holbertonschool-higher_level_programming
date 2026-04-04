#!/usr/bin/python3
"""MyInt is rebel that inherits from int."""


class MyInt(int):
    """Subclass of int except == and != operations are reversed."""

    def __init__(self, value):
        """Initialize value."""
        self.value = value

    def __eq__(self, other):
        """Override the '==' operator.

        Return True if they are conventionally unequal, False otherwise.
        """
        return int(self) != other

    def __ne__(self, other):
        """Override the '!='.

        Return True if they are conventionally equal, false otherwise.
        """
        return int(self) == other
