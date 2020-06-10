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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """gets private instance attribute x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets private instance attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """gets private instance attribute y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets private instance attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns area calculation for rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the rectangle instance with '#'
        with offsets x and y taken into account"""
        for vertical in range(self.y):
            print("")
        for row in range(self.height):
            print(" "*self.x, end="")
            print("#"*self.width)

    def __str__(self):
        """override __str__ with new string in the format
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        str_rep = "[Rectangle] ({}) {}/{} - {}/{}".format(
            str(self.id), str(self.x), str(self.y),
            str(self.width), str(self.height))
        return (str_rep)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute of Rectangle"""
        attr_list = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            for kw in kwargs:
                if kw == "id":
                    self.id = (kwargs[kw])
                if kw == "width":
                    self.width = (kwargs[kw])
                if kw == "height":
                    self.height = (kwargs[kw])
                if kw == "x":
                    self.x = (kwargs[kw])
                if kw == "y":
                    self.y = (kwargs[kw])

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""
        dict_rep = {}
        dict_rep["id"] = self.id
        dict_rep["width"] = self.width
        dict_rep["height"] = self.height
        dict_rep["x"] = self.x
        dict_rep["y"] = self.y
        return dict_rep
