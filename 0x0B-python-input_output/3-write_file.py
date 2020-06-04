#!/usr/bin/python3
"""defines function to write string to text file"""


def write_file(filename="", text=""):
    """writes string to text file"""
    with open(filename, 'w') as f:
        return f.write(text)
