import heapq
#By default in a heap, smallest value is at index 0
#By default in python, we have a min-heap
#Smallest here first converts the array in a heap
#Then pops the smallest value/element, preserving the heap
def smallest(array):
    heapq.heapify(array)
    heapq.heappop(array)
    return array[0]

#heapq.push adds a value while preserving the heap
def push(array):
    h = []
    for num in array:
        heapq.heappush(h, num)
    return h

print(push([8,4,7,2,3,4,5]))
