#!/usr/bin/env python3
"""
Module containing the Animal abstract base class and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing a generic animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a dog.
    """

    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a cat.
    """

    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"
