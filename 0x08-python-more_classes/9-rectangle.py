#!/usr/bin/python3
"""
Created on 4th April, 2023
A rectangle class
"""

class Rectangle:
    """rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        deletes an instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """
        str method to print rectangle
        returns a string rep of given param
        """
        string = ''
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
                if j == self.__width -1 and i == self.__height - 1:
                    break
                if j == self.__width - 1:
                    string += "\n"
        return string

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def area(self):
        """
        Property width to retrieve it
        Returns:
            area: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height + self.__height + self.__width + self.__width

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


    def area(self):
        """
        Property width to retrieve it
        Returns:
            area: The area of the rectangle
        """
        return self.__width * self.__height

    @classmethod
        def square(cls, size=0):
        """
        class method tat defines a quare
        """
            return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        rect_1: an instance of rectangle
        rect_2: an instance of rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        if rect_1 == rect_2:
            return rect_1
