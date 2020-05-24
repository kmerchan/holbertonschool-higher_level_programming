#!/usr/bin/python3
"""creates class Rectangle"""


class Rectangle:
    """defines class Rectangle with private instance attributes width/height
and public instance methods to return the rectangle area and primeter"""

    def __init__(self, width=0, height=0):
        """instantiates class instance with optional width/height attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """calculates perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))
