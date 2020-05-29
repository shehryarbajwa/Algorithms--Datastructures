class MultiStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, item):
        if len(self.stacks) and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    
    def pop(self):
        if len(self.stacks) == 0:
            return None
        item = self.stacks[-1].pop()
        #After removing last element, if the last stack becomes empty, we remove it from stack list
        #[[1,2],[2]] -> [[1,2]]
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return item
    
    def pop_at(self, stack_number):
        #Edge case
        #Stacks are [[1,2],[3,4]]
        #We are asked to pop at stack number 2
        #Our stacks are in fact 0 and 1
        #When stack number is > or equal to len of stacks, we are running one ahead of array index
        if (stack_number < 0) or stack_number >= len(self.stacks):
            return None
        if len(self.stacks[stack_number]) == 0:
            return None
        return self.stacks[stack_number].pop()

import unittest

class Tests(unittest.TestCase):
    def test_case_1(self):
        stack = MultiStack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop_at(0), 3)


if __name__ == "__main__":
    unittest.main()
