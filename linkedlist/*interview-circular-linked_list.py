"""
Algorithm to check whether the linked list is a loop
"""

class Node:
    def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
    def __init__(self, init_List=None):
        self.head = None

        if init.list:
            for value in init_List:
                self.append(value)
    
    def append(self,value):

        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head

        while node.next:
            node = node.next
        
        node = Node(value)
        return


def isCircular(LinkedList):

    slow = LinkedList.head
    fast = LinkedList.head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False


