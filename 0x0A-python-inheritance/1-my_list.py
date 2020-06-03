#!/usr/bin/python3
"""defines class MyList"""


class MyList(list):
    """class that inherits from list
    with public instance method to print sorted list"""

    def print_sorted(self):
        print(sorted(self))
