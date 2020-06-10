#!/usr/bin/python3
"""defines Square class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class for Square instances with
    attributes from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes Square instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """gets private instance attribute size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """sets private instance attribute size and
        uses to set width and height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """override __str__ with new string in the format
        [Square] (<id>) <x>/<y> - <size>"""
        str_rep = "[Square] ({}) {}/{} - {}".format(
            str(self.id), str(self.x), str(self.y), str(self.width))
        return (str_rep)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute of Square"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for kw in kwargs:
                if kw == "id":
                    self.id = (kwargs[kw])
                if kw == "size":
                    self.size = (kwargs[kw])
                if kw == "x":
                    self.x = (kwargs[kw])
                if kw == "y":
                    self.y = (kwargs[kw])

    def to_dictionary(self):
        """returns dictionary representation of a Square"""
        dict_rep = {}
        dict_rep["id"] = self.id
        dict_rep["size"] = self.size
        dict_rep["x"] = self.x
        dict_rep["y"] = self.y
        return dict_rep
