def single_cycle_check(array):
    count = 0
    startIdx = 0

    while count < len(array):
        if count > 1 and startIdx == 0:
            return False
        count += 1
        startIdx = get_next_index(startIdx, array)
    return count == 0

def get_next_index(startIdx, array):
    jump = array[startIdx]
    nextIndex = (startIdx + jump) % len(array)
    #For negative indexes
    return nextIndex if nextIndex >= 0 else nextIndex + len(array)