#!/usr/bin/python3
"""Mylist inherits from list, it has method to print the list in asc order."""


class MyList(list):
    """Inherit from list superclass."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
