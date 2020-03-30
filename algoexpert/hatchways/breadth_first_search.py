
import unittest

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(Node(child))

    def breadth_first_search(self, array):

        queue = [self]

        while len(queue):
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


