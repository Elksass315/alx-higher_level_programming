#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle from BaseGeometry class."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): new Rectangle height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the str() of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
