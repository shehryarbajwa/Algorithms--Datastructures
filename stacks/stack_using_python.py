#Building a Stack in Python
#A stack is a data structure that consists of two main operations: push and pop. 
#A push is when you add an element to the top of the stack and a pop is when you remove an element from the top of the stack. 
#Python 3.x conviently allows us to demonstate this functionality with a list. When you have a list such as [2,4,5,6] you can decide which end of the list is the bottom and the top of the stack respectivley. 
#Once you decide that, you can use the append, pop or insert function to simulate a stack. We will choose the first element to be the bottom of our stack and therefore be using the append and pop functions to simulate it. 
#Give it a try by implementing the function below!

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
            return self.items.pop()


foo = Stack()

foo.push(5)
foo.push(10)
foo.push(15)
foo.push(100)
foo.pop()
print(foo.pop())
foo.pop()
print(foo.pop())
print(foo.pop())
print(foo.items)
