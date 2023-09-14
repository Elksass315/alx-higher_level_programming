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

    def __str__(self):
        """overloading __str__ method return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
