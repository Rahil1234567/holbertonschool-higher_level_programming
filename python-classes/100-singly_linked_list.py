#!/usr/bin/python3
"""Module for a singly linked list"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data with validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node with validation"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initialize the linked list"""
        self.__head = None

    def __str__(self):
        """Define the print behavior for the list"""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position"""
        new_node = Node(value)

        # Case 1: List is empty or new value is smaller than head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Case 2: Traverse to find the correct spot
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
