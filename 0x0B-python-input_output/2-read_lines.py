#!/usr/bin/python3
"""defines function to read n lines of a text file"""


def read_lines(filename="", nb_lines=0):
    """reads nb_lines of text file"""
    if nb_lines <= 0:
        with open(filename) as f:
            print(f.read(), end="")
    else:
        with open(filename) as f:
            for i in range(nb_lines):
                print(f.readline(), end="")
