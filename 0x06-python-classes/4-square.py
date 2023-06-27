#!/usr/bin/python3
"""class square"""

class Square:
    """square class"""

    def __init__(self, size=0):
        """new square

        args:
            size (int): square size.
        """

        self.size = size

    @@property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)
