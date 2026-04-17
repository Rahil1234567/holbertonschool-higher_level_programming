#!/usr/bin/env python3
"""
Module demonstrating Mixins through SwimMixin, FlyMixin, and the Dragon class.
"""


class SwimMixin:
    """Provides swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that composes behaviors from SwimMixin and FlyMixin.
    """

    def roar(self):
        """Prints a roaring message unique to the Dragon."""
        print("The dragon roars!")
