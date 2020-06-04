#!/usr/bin/python3
"""defines function that counts number of lines read from file"""


def number_of_lines(filename=""):
    """returns number of lines read from text file"""
    count = 0
    with open(filename) as f:
        while f.readline() is not "":
            count += 1
    return count
