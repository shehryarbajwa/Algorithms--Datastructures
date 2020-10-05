import heapq
from collections import Counter
#[1,1,1,2,2,3]
#Counting takes O(N) and adding to heap takes O(log k) thus total complexity is O(N log k)
#Space complexity is O(N) + O(K) equals O(N + K)
def kth_frequent_element(array, k):
    if not array:
        return []
    if len(array) == 1:
        return array
    h = []
    count = Counter(array)
    for key, value in count.items():
        heapq.heappush(h, (-count[key], key))

    i = 0
    output = set()
    while i < k:
        freq, item = heapq.heappop(h)
        output.add(item)
        i += 1
    return output

print(kth_frequent_element([1,1,1,2,2,3],2))

    
