"""
Linked List practice
"""


class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def prepend(self, value):
# Prepend a node to the beginning of the list
    
    if self.head is None :
        self.head = Node(value)
        return
    
    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head