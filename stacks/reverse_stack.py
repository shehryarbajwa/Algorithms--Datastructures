class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def reverse_stack(stack):
    #Create a holder stack. Initially empty
    holder_stack = Stack()
    #While the stack is not empty
    while not stack.is_empty():
    #Pop the element from the original stack. Meaning the top item which was added last i.e [1,2,3,4]
        popped_element = stack.pop()
        #element popped is 4
    #Push that element to the new stack so new stack is [4,3,2,1]. Last item added at the top is 1
        holder_stack.push(popped_element)
    #Recurse to reverse the original stack now
    _recursion(stack, holder_stack)

def _recursion(stack, holder_stack):

    if holder_stack.is_empty():
        return
    #Pop the element from the holder_stack which is 1. Left with 4,3,2. 
    popped_element = holder_stack.pop()
    #Then we do the recursion, where we get the popped element again which will be 2
    #Then we do the recursion again, where the popped element will be 3
    #Then we do the recursion again, where the popped element will be 4
    #Basically we will recurse 4 times
    _recursion(stack, holder_stack)
    stack.push(popped_element)

