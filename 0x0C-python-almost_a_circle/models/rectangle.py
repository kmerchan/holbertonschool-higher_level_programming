#!/usr/bin/python3
"""defines Rectangle class that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """class for Rectangle instances with
    private instance attributes width, height, x, and y"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets private instance attribute width"""
        self.__width = value

    @property
    def height(self):
        """gets private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets private instance attribute height"""
        self.__height = value

    @property
    def x(self):
        """gets private instance attribute x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets private instance attribute x"""
        self.__x = value

    @property
    def y(self):
        """gets private instance attribute y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets private instance attribute y"""
        self.__y = value
