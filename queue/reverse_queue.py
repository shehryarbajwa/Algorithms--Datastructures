# Write a function that takes a queue as an input and returns a reversed version of it.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, data):
        #Enqueue means adding to the tail of the linked list
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        #Dequeue means removing from the head of the linked list
        if self.is_empty():
            return None
        temp = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head.value is None:
            return None
        else:
            return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, data):
        new_value = Node(data)

        if self.head is None:
            self.head = new_value
        else:
            new_value.next = self.head
            self.head = new_value
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return temp
    
    def size(self):
        return self.num_elements

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def is_empty(self):
        return self.num_elements == 0


    
def reverse_queue(queue):
    stack = Stack()

    while not queue.is_empty():
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())