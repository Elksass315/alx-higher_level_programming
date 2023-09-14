#!/usr/bin/python3
"""square class inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """new Square constructor.

        Args:
            size (int): new Square size.
            x (int): new Square x coordination.
            y (int): new Square y coordination.
            id (int): new Square id.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """squre size getter and setter"""
        return self.width

    @size.setter
    def size(self, v):
        self.width = v
        self.height = v

    def __str__(self):
        """overloading __str__ method return
            [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Update the class Square.

        Args:
            *args (ints): New attribute values.
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            **kwargs (dict): the new key/value attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
