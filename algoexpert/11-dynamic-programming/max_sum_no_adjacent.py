#Time Complexity O(N)
#Space Complexity O(N)
def max_sum_adjacent_num(array):
    if len(array) == 0:
        return False
    
    if len(array) == 1:
        return array[0]

    max_sums = array[:]
    max_sums[1] = max(array[0], array[1])
    
    for i in range(2, len(array)):
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])

    return max_sums[-1]

#Time Complexity O(N)
#Space Complexity O(1)
def max_sums_dynamic(array):
    if len(array) == 0:
        return False
    if len(array) == 1:
        return array[0]

    second = array[0]
    first = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first
    

