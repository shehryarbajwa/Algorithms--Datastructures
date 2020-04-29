
class DynamicArray:
    def __init__(self):
        self.array = [0] * 2
        self.capacity = 2
        self.current_index = 0

    def add(self, item):

        if (self.capacity == self.current_index):
            self.resizeArray()

        self.array[self.current_index] = item
        self.current_index += 1

    def remove(self):
        if (self.current_index == 0):
            raise Exception("Cannot remove from empty list")
        self.current_index -= 1

    def get(self, index):
        if (index < 0 or index > self.current_index):
            raise Exception("Index out of range")
        return self.array[index]

    def size(self):
        return len(self.array)


    def resizeArray(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.array):
            new_array[i] = self.array[i]
        self.array = new_array