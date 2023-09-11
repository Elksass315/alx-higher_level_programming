#!/usr/bin/python3
"""Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class."""

    def __init__(self, size):
        """a new square.

        Args:
            size (int): new square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
