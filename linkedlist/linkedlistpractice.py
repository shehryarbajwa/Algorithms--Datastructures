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


linked_list = LinkedList()
linked_list.prepend(3)
linked_list.append(4)
linked_list.append(6)
linked_list.remove(4)

for obj in linked_list:
    print(obj.value)