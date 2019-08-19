"""
Linked List practice
"""


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# Prepend a node to the beginning of the list
    def prepend(self, value):
    
        if self.head is None :
           self.head = Node(value)
           return
    
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

# Append an element to the list
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
    

        node = self.head

        while node.next:
            node = node.next

        node.next = Node(value)

# Search a node within a list

    def search(self, value):

        if self.head is None:
            return None

        current_node = self.head

        while current_node:

            if current_node.value == value:
                return current_node
            
            current_node = current_node.next
        
        raise ValueError('Value not found in the list')

# Remove a node from the list

    def remove(self,value):

        if self.head is None:
            return None
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        node = self.head

        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError('Value not found in the list')

# Pop, which means to return the first node's value and delete the node from the list

    def pop(self):

        if self.head is None:
            return None
        
        node = self.head
        self.head = self.head.next
        return node.value

# Insert a node with a value at the position provided

    def insert(self,value,position):

        if position == 0:
            self.prepend(value)
            return
        
        index = 0
        node = self.head

        while node.next and position <= index:

            if (position - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return
            index += 1
            node = node.next

        else:
            self.append(value)

# Return the size of the linked list

def size(self):

    size = 0
    node = self.head

    while node:
        size += 1
        node = node.next
    
    return size



linked_list = LinkedList()
linked_list.prepend(3)
linked_list.append(4)
linked_list.append(6)
linked_list.remove(4)

