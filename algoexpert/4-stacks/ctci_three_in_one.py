class MultiStack:
    
    def __init__(self, stacksize):
        self.stacknum = 3
        self.stackcapacity = stacksize
        self.array = [0 for _ in range(stacksize * self.stacknum)]
        self.size = [0] * self.stacknum

    def push(self, item, stacknum):
        if self.is_full(stacknum):
            raise ValueError("Stack is full")
        self.size[stacknum] += 1
        self.array[self.indexTop(stacknum)] = item

    def pop(self, stacknum):
        if self.is_empty(stacknum):
            raise ValueError("Stack is empty")
        value = self.array[self.indexTop(stacknum)]
        self.array[self.indexTop(stacknum)] = 0
        self.size[stacknum] -= 1
        return value


    def is_empty(self, stacknum):
        return self.size[stacknum] == 0

    def is_full(self, stacknum):
        return self.size[stacknum] == self.stackcapacity

    def indexTop(self, stacknum):
        offset = stacknum * stackcapacity
        size = self.size[stacknum]
        return offset + size - 1


    


       

def ThreeInOne():
    newstack = MultiStack(2)
    print(newstack.IsEmpty(1))
    newstack.Push(3, 1)
    print(newstack.Peek(1))
    print(newstack.IsEmpty(1))
    newstack.Push(2, 1)
    print(newstack.Peek(1))
    print(newstack.Pop(1))
    print(newstack.Peek(1))
    newstack.Push(3, 1)

ThreeInOne()