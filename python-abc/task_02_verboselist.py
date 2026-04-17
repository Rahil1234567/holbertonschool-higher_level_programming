#!/usr/bin/env python3
"""
Module providing a VerboseList class that notifies of modifications.
"""


class VerboseList(list):
    """
    A list subclass that prints notifications upon modification.
    """

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list and prints a notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Prints a notification before removing an item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Prints a notification before popping an item."""
        # We need to retrieve the item to print it before removal
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
