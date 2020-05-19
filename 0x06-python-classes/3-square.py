#!/usr/bin/python3
"""creates class Square with
private instance attribute size and public instance method"""


class Square:
    """defines class with instantiated and validated private instance attribute
and public instance method."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates and returns current square area"""
        return(self.__size * self.__size)
