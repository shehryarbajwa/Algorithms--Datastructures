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
        self.tail = None

def prepend(self, value):
# Prepend a node to the beginning of the list
    
    if self.head is None :
        self.head = Node(value)
        return
    
    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head

def append(self, value):
# Append an element to the list

    if self.head is None:
        self.head = Node(value)
        self.tail = self.head
        return
    

    node = self.head

    while node.next:
        node = node.next

    node.next = Node(value)