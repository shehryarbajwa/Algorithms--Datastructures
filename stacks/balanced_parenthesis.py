#Use stacks to make sure that the parenthesis are balanced in mathematical expressions

class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)
