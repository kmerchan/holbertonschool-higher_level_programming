#!/usr/bin/python3
"""defines function to appends string to text file"""


def append_write(filename="", text=""):
    """appends string to text file"""
    with open(filename, 'a') as f:
        return f.write(text)
