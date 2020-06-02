#!/usr/bin/python3
"""define function to return list of available attributes and methods"""


def lookup(obj):
    """returns list of available attributes and methods of an object"""

    return (dir(obj))
