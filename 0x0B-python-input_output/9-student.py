#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """student class representation."""

    def __init__(self, first_name, last_name, age):
        """Initialization of a new Student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Will returne a dictionary representation of the Student."""
        return self.__dict__
