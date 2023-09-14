#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """New Rectangle constructor

        Args:
            width (int): new Rectangle width
            height (int): new Rectangle height
            x (int): new Rectangle x coordinate
            y (int): new Rectangle y coordinate
            id (int): new Rectangle id

            Raises:
            TypeError: If either one of args not an int.
            ValueError: If either onr of args < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """set and get the width."""
        return self.__width

    @width.setter
    def width(self, v):
        if type(v) != int:
            raise TypeError("width must be an integer")
        if v <= 0:
            raise ValueError("width must be > 0")
        self.__width = v

    @property
    def height(self):
        """set and get the height."""
        return self.__height

    @height.setter
    def height(self, v):
        if type(v) != int:
            raise TypeError("height must be an integer")
        if v <= 0:
            raise ValueError("height must be > 0")
        self.__height = v

    @property
    def x(self):
        """set and get the x."""
        return self.__x

    @x.setter
    def x(self, v):
        if type(v) != int:
            raise TypeError("x must be an integer")
        if v < 0:
            raise ValueError("x must be >= 0")
        self.__x = v

    @property
    def y(self):
        """set and get the y."""
        return self.__y

    @y.setter
    def y(self, v):
        if type(v) != int:
            raise TypeError("y must be an integer")
        if v < 0:
            raise ValueError("y must be >= 0")
        self.__y = v

    def area(self):
        """area value of the Rectangle instance."""
        return self.width * self.height
