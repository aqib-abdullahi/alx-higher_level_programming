#!/usr/bin/python3
"""contains square class that inherits form the rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inherits from the rectangle class in previous tasks"""
    def __init__(self, size):
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """str method"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
