class Queue:

    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        #-1 means there are no elements in the queue and it is empty
        self.front_index = -1
        self.queue_size = 0

    def deque(self, value):
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            return None
        return self.arr[self.front_index]