import unittest

class Queue:
    def __init__(self, initial_size = 10):
        self.array = [None for _ in range(initial_size)]
        self.next_index = 0
        self.queue_size = 0
        self.front_index = None

    def enqueue(self,value):

        if self.queue_size == len(self.array):
            self.handle_excess_capacity()

        self.array[self.next_index] = value
        self.next_index += 1
        self.queue_size += 1
        
        if self.front_index is None:
            self.front_index = 0

        return self

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        return self.array[self.front_index]

    def dequeue(self):

        if self.is_empty():
            self.front_index = None
            self.next_index = 0
            return None

        value = self.array[self.front_index]
        self.array[self.front_index] = None
        self.next_index -= 1
        self.queue_size -= 1
        self.front_index += 1

        return value

    def handle_excess_capacity(self):
        old_array = self.array
        self.array = [None for _ in range(2 * len(old_array))]

        index = 0
        for i in range(self.front_index, len(old_array)):
            self.array[index] = old_array[i]
            index += 1

        self.front_index = 0
        self.next_index = index


class Tests(unittest.TestCase):
    def test_case_1(self):
        node_1 = Queue()
        node_1.enqueue(10).enqueue(20).enqueue(30).enqueue(40).enqueue(50).enqueue(60).enqueue(70).enqueue(80).enqueue(90).enqueue(100).enqueue(110)
        self.assertEqual(node_1.array, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, None, None, None, None, None, None, None, None, None])
    
    def test_case_2(self):
        node_1 = Queue()
        node_1.enqueue(10).enqueue(20).enqueue(30).enqueue(40).enqueue(50).enqueue(60).enqueue(70).enqueue(80).enqueue(90).enqueue(100).enqueue(110).enqueue(120).enqueue(130)
        node_1.dequeue()
        self.assertEqual(node_1.array, [None, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, None, None, None, None, None, None, None])



if __name__ == "__main__":
    unittest.main()