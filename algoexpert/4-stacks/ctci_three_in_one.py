import unittest

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

    def peek(self, stacknum):
        if self.is_empty(stacknum):
            raise ValueError("Stack is empty")
        value = self.array[self.indexTop(stacknum)]
        return value

    def is_empty(self, stacknum):
        return self.size[stacknum] == 0

    def is_full(self, stacknum):
        return self.size[stacknum] == self.stackcapacity

    def indexTop(self, stacknum):
        offset = stacknum * self.stackcapacity
        size = self.size[stacknum]
        return offset + size - 1


class Tests(unittest.TestCase):
    def test_case_1(self):
        three_stacks = MultiStack(2)
        three_stacks.push(1, 0)
        three_stacks.push(2, 0)
        three_stacks.push(3,1)
        three_stacks.push(4,1)
        three_stacks.push(5,2)
        three_stacks.push(6,2)
        self.assertEqual(three_stacks.is_full(2), True)
        self.assertEqual(three_stacks.is_empty(2), False)


if __name__ == '__main__':
    unittest.main()