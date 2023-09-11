#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """No implementipn yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """is the  parameter an integers.

        Args:
            name (str): the parameter name.
            value (int): validate this parmeter.
        Raises:
            TypeError: If not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
