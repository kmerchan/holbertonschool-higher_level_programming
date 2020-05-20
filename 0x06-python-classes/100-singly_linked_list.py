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
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """defines class for singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """insert new node"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            tmp = self.__head
            if tmp.data > new_node.data:
                new_node.next_node = tmp
                self.__head = new_node
                return
            while tmp.next_node is not None:
                tmp2 = tmp.next_node
                if tmp2.data < new_node.data:
                    tmp = tmp2
                else:
                    new_node.next_node = tmp.next_node
                    tmp.next_node = new_node
                    return
            tmp.next_node = new_node

    def stringrep(self):
        strrep = ""
        tmp = self.__head
        while tmp is not None:
            datavalue = tmp.data
            strrep = strrep + str(datavalue)
            tmp = tmp.next_node
            if tmp:
                strrep = strrep + "\n"
        return strrep

    def __repr__(self):
        return(self.stringrep())
