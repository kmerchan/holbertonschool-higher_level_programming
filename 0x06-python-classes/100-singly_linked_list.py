#!/usr/bin/python3
"""creates class Node to define linked list node & class SinglyLinkedList"""


class Node:
    """defines class for singly linked list node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter for data attribute"""
        return(self.__data)

    @data.setter
    def data(self, value):
        """setter for data attribute"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ getter for next_node attribute"""
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """setter for next_node attribute"""
        if type(value) is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """defines class for singly linked list"""

    def __init__(self):
        SinglyLinkedList.__head = None

    def sorted_insert(self, value):
        pass
