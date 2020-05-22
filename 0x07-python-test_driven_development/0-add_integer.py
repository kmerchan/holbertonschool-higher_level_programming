#!/usr/bin/python3
"""defines a function to add 2 integers"""


def add_integer(a, b=98):
    """add 2 integers or floats cast as integers, default 2nd int is 98"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
