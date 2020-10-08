import heapq
def ugly_number(n):
    seen = set()
    seen.add(1)
    arr = []
    heap = []
    heapq.heappush(heap, 1)
    for j in range(1690):
        current = heapq.heappop(heap)
        arr.append(current)
        
        for i in [2,3,5]:
            new_element = current * i
            if new_element not in seen:
                seen.add(new_element)
                heapq.heappush(heap, new_element)

    return arr[n - 1]

print(ugly_number(10))

