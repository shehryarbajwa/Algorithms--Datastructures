class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    #O(n) time complexity
    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array

    #O(log(n)) time complexity
    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1

        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if heap[idx_to_swap] < heap[current_idx]:
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                break
    
    #O(log(n)) time complexity
    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2
    
    #O(1)
    def peek(self):
        return self.heap[0]

    #O(logn)
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    #O(logn)
    def insert(self, value):
        self.head.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, i, j , heap):
        heap[i], heap[j] = heap[j], heap[i]