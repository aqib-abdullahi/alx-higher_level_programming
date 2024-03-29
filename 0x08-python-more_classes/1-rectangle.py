#!/usr/bin/python3
"""
Created on 3rd April, 2023
A rectangle class
"""

class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """
        Init method for Rectangle
        Attributes:
            width: The width of the rectangle
            height: The height of the rectangle
        self.width = width
        self.height = height
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Property height to retrieve it
        Returns:
            height: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectangle
        Attributes:
            height: The height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Property width to retrieve it
        Returns:
            width: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width of the rectangle
        Attributes:
            width: The width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
