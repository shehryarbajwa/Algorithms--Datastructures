class Queue:

    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        self.storage.pop(0)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.size())
q.dequeue()
print(q.size())