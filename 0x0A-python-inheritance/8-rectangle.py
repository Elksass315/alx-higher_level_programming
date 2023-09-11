#!/usr/bin/python3
"""class Rectangle inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle inherits from BaseGeometry."""

    def __init__(self, width, height):
        """new Rectangle.

        Args:
            width (int):  Rectangle width.
            height (int): new Rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
