#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
    
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """new Rectangle

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
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

        s = []
        for i in range(self.__height):
            [s.append(str(self.print_symbol) for j in range(self.__width)]
            if i != self.__height - 1:
                s.append("\n")
        return ("".join(s))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        str_represntation = "Rectangle(" + str(self.__width)
        str_represntation += ", " + str(self.__height) + ")"
        return (str_represntation)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
