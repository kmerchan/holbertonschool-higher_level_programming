#!/usr/bin/python3
"""defines rebel integer class"""


class MyInt(int):
    """rebel integer class that switches == and !="""
    def __eq__(self, other):
        """when equal is called, return not equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """when not equal is called, return equal"""
        return super().__eq__(other)
