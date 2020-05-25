class ThreeOneStack:
    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexofTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def is_empty(self, stacknum):
        return self.sizes[stacknum] == 0

    def is_full(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

       

three = ThreeOneStack()
three.push(3)+.0
