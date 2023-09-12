#!/usr/bin/python3
"""Student class."""


class Student:
    """student."""

    def __init__(self, first_name, last_name, age):
        """new Student.

        Args:
            first_name (str): student first name.
            last_name (str): student last name.
            age (int): student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict representation of the Student info."""
        return self.__dict__
