#!/usr/bin/python3

"""Declare a Square class."""


class Square:
    """Representation of  a square."""

    def __init__(self, size=0, position=(0, 0)):
        """ New square initialization.

        Args:
            size (int): new square size.
            position (int, int): New square's position.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Set actual position."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the actual area's square."""
        return (self.__size * self.__size)

    def my_print(self):
        """show the square together with the character #."""
        if self.__size == 0:
            print("")
            return

        [print("") for a in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for b in range(0, self.__position[0])]
            [print("#", end="") for c in range(0, self.__size)]
            print("")

    def __str__(self):
        """Declare the representation of a Square print()."""
        if self.__size != 0:
            [print("") for a in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for b in range(0, self.__position[0])]
            [print("#", end="") for c in range(0, self.__size)]
            if a != self.__size - 1:
                print("")
        return ("")
