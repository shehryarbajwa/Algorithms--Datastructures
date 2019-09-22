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
    #We can reverse a queue using a stack
    stack = Stack()

    #First we have to empty out all the elements of the queue e.g queue is 2 -> 3 -> 4    2 at bottom, 4 at top
    # Each element from the queue starting with 2 will be pushed to an emtpy stack 
    #The stack will have its first element at 2, then it will push on top of it 2 -> 3 -> 4
    while not queue.is_empty():
        stack.push(queue.dequeue())

    #Now we will iterate over the stack. Since in stack we can find the head node, by using pop, we can remove it
    # So we will remove items from the stack starting with 4 then 3 then 2 and add it to the queue
    # Now the queue has 4 -> 3 -> 2
    while not stack.is_empty():
        queue.enqueue(stack.pop())