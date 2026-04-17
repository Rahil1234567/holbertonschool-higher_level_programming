#!/usr/bin/env python3
"""
Module for CountedIterator, which tracks the number of items iterated.
"""


class CountedIterator:
    """
    A class that wraps an iterator and keeps track of how many items
    have been fetched.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator from an iterable and sets the counter to 0.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Returns the current number of items that have been iterated.
        """
        return self.counter

    def __next__(self):
        """
        Fetches the next item, increments the counter, and returns the item.
        Raises StopIteration if no more items are available.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            # Re-raise the exception to signal the end of iteration
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator object itself. 
        Required to make this class an 'iterable' as well.
        """
        return self
