#!/usr/bin/python3
"""contains rectangle class that inherits from the BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """initialization method"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """function return the area"""
        return self.__width * self.__height

    def __str__(self):
        """the string function or method"""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
