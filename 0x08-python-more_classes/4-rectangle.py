#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rectangle area"""
        rectangleArea = self.width * self.height
        return rectangleArea

    def perimeter(self):
        """perimeter"""
        if self.width == 0 or self.height == 0:
            return 0

    def __str__(self):
        """string representation of the Rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        str_represntation = []
        for i in range(self.__height):
            [str_represntation.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                str_represntation.append("\n")
        return ("".join(str_represntation))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        str_represntation = "Rectangle(" + str(self.__width)
        str_represntation += ", " + str(self.__height) + ")"
        return (str_represntation)
