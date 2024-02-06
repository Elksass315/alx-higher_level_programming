#!/usr/bin/python3
"""empty BaseGeometry class."""


class BaseGeometry:
    """Represent baseclass geometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

class Square(Rectangle):

    def __init__(self, size):
        super().integer_validator("size", size)

