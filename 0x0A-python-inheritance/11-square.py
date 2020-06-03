#!/usr/bin/python3
"""defines class Square that inherits from Rectangle"""


Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """class for square that inherits from Rectangle
    with method for area and string representation"""
    def __init__(self, size):
        """initializes Square instance"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)

    def __str__(self):
        """string representation of Square"""
        str_rep = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return str_rep
