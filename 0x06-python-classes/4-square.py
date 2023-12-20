#!/usr/bin/python3

"""Declare a Square class."""


class Square:
    """Representation of  a square."""
    def __init__(self, size=0):
        """ New square initialization.

        Args:
            size (int): new square size.
        """
        self.size = size

    @property
    def size(self):
        """set actual size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the actual area's square."""
        return (self.__size * self.__size)
