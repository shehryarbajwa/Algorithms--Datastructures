#Stack has push and pop functions in it. Our stack will also have is_empty and size as methods


import unittest

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


class Tests(unittest.TestCase):
    def test_case_1(self):
        node = Stack()
        node.push(15).push(10).push(12).push(13)

        self.assertEqual(node.array, [15, 10, 12, 13, None, None, None, None, None, None])

    def test_case_2(self):
        node = Stack()
        node.push(15).push(10).push(12).push(13).pop()

        self.assertEqual(node.array, [15, 10, 12, None, None, None, None, None, None, None])


if __name__ == '__main__':
    unittest.main()