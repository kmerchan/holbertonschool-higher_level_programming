#!/usr/bin/python3
"""defines class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class for square that inherits from Rectangle
    with method for area"""
    def __init__(self, size):
        """initializes Square instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)
