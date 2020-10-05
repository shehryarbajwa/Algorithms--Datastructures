
import heapq
#Time Complexity O(N) building heap, worst case O(N log(N))
#Space Complexity O(N) for storing in max_heap

def kth_largest_element(array, k):
    max_heap = []
    for num in array:
        heapq.heappush(max_heap, (num) * -1)
    
    i = 0
    while i < k:
        res = heapq.heappop(max_heap)
        i += 1
    return res * -1

def kth_largest_element_in_place(array, k):
    for index, num in enumerate(array):
        array[index] = num * -1
    
    heapq.heapify(array)

    i = 0
    while i < k:
        res = heapq.heappop(array)
        i += 1
    return res * -1

print(kth_largest_element([8,4,7,2,3,4,5],3))
print(kth_largest_element_in_place([8,4,7,2,3,4,5],3))

