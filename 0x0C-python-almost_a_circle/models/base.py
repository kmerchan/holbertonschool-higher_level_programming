#!/usr/bin/python3
"""defines Base class"""


class Base():
    """manages id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes to given id or
        increases class nb_objects and sets as default id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
