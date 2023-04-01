#!/usr/bin/python3
"""Created on April 1, 2023."""

class Square:
    """ A square class"""

    def __init__(self, size=0):
        """Initialize square
        Args:
            size (int): Size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        """returns square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size to value"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = value
    def area(self):
        """returns the area of square"""
        return self.__size ** 2
