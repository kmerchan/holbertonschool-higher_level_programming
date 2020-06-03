#!/usr/bin/python3
"""defines function to see if object is an instance of a class
that is a subclass of the specified class"""


def inherits_from(obj, a_class):
    """returns True if object is an instance of a subclass
    of the given class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
