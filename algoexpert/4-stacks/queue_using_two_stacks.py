class Stack:
    def __init__(self, initial_size = 10):
        self.array = [None for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):

        if self.next_index == len(self.array):
            self.handle_stack_capacity()

        self.array[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1
        return self

    def handle_stack_capacity(self):
        old_array = self.array

        self.array = [None for _ in range(2 * len(old_array))]
        for index, element in enumerate(old_array):
            self.array[index] = element

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        #Edge case after popping numbers we end up with no elements to pop
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        self.array[self.next_index] = None
        return self

class QueueTwoStacks:
    def __init__(self):
        self.stackOne = Stack()
        self.stackTwo = Stack()

    def enqueue(self, element):
        self.stackTwo.push(element)

    def size(self):
        return self.stackOne.size() + self.stackTwo.size()

    def shiftStacks(self):
        if self.stackOne.is_empty():
            while not self.stackTwo.is_empty():
                self.stackOne.push(self.stackTwo.pop())

    def dequeue(self):
        shiftStacks()
        return self.stackOne.pop()

    def peek(self):
        shiftStacks()
        return self.stackOne.peek()