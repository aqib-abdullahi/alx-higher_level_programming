#!/usr/bin/python3
"""contains a square class that inherits from the rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from the rectangle class"""
    def __init__(self, size):
        """initialization method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
