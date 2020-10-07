import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.array = nums
        self.k = k

        heapq.heapify(self.array)

        while len(self.array) > k:
            heapq.heappop(self.array)

    def add(self, value):
        heap_top = 0

        if len(self.array) < self.k:
            heapq.heappush(self.array, value)
        else:
            heapq.heappush(self.array, value)
            heapq.heappop(self.array)
        return self.array[heap_top]

