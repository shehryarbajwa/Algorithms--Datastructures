class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            self.items.pop()

class Queue:

    def __init__(self):
        

    