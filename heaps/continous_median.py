class ContinousMedian:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNC, [])
        self.greaters = Heap(MIN_HEAP_FUNC, [])
        self.median = None


    def insert(self, number):
        #Check if number is < lowers root or if lowers doesnt exist
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.rebalance_heaps()
        self.update_median()

    def rebalance_heaps(self):
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())


    def update_median(self):
        #Both have same length
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) // 2
        #if lowers has one more than greater
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()





class Heap:
    def __init__(self, comparisonFunc, array):
        self.comparisonFunc = comparisonFunc
        self.heap = self.build_heap(array)
        self.length = len(self.heap)

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2

        #Go from end all way to top
        for current_idx in reversed(range(first_parent_idx)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array


    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            #If child_two is smaller than child one then we swap with child two
            if child_two_idx != -1:
                if self.comparisonFunc(heap[child_two_idx], heap[child_one_idx]):
                    idx_to_swap = child_two_idx
                else:
                    idx_to_swap = child_one_idx
            else:
                idx_to_swap = child_one_idx

            if self.comparisonFunc(heap[idx_to_swap], heap[current_idx]):
                self.swap(idx_to_swap, current_idx, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def peek(self):
        return self.heap[0]


    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2

        while current_idx > 0:
            if self.comparisonFunc(heap[current_idx], heap[parent_idx]):
                self.swap(current_idx, parent_idx, self.heap)
                current_idx = parent_idx
                parent_idx = (current_idx - 1) // 2
            else:
                return


    #Remove root value - minimum value
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.length -= 1
        self.sift_down(0, self.length - 1, self.heap)
        return value_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.sift_up(self.length -  1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


def MAX_HEAP_FUNC(a, b):
    return a > b

def MIN_HEAP_FUNC(a, b):
    return a < b