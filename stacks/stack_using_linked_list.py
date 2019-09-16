#Implement a stack using a linked list
#Previously, we looked at how to implement a stack using an array. 
# While that approach does work, we saw that it raises some concerns with time complexity.
# For example, if we exceed the capacity of the array, we have to go through the laborious process 
# of creating a new array and moving over all the elements from the old array.
# What if we instead implement the stack using a linked list? Can this improve our time complexity? 
# Let's give it a try.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        #If the stack is empty then we assign the new Node to the head
        if self.head is None:
            self.head = new_node
        #If the stack is not empty, then we add an element to the top of the stack meaning to the left of the head node
        #Once we assign the next value of the new node to the head value, we then assign the head to the new value which is the top value

        else:
            new_node.next = self.head
            self.head = new_node
        #Since we have added a new element, that will increase our number of elements by 1
        self.num_elements += 1
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value
