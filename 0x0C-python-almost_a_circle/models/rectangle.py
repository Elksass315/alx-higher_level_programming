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

    def display(self):
        """prints in stdout the Rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for hi in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wi in range(self.width)]
            print("")

    def __str__(self):
        """__str__ method so that it returns
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """update the Rectangle

        Args:
            *args (list of ints): New attribute values.
            **kwargs (ket/value of int): the assigning  key/value argument
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
