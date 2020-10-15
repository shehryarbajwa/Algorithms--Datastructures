def shifted_binary_search(array, target):
    return shifted_binary_search(array, target, 0, len(array) - 1)

def shifted_binary_search(array, target, left, right):
    if left > right:
        return -1
    mid_idx = (left + right) // 2
    potential_match = array[mid_idx]
    left_num = array[left]
    right_num = array[right]

    if target == potential_match:
        return mid_idx
    elif left_num <= potential_match:
        if target < potential_match and target >= left_num:
            return shifted_binary_search(array, target, left, mid_idx - 1)
        else:
            return shifted_binary_search(array, target, mid_idx + 1, right)
    else:
        if target > potential_match and target <= right_num:
            return shifted_binary_search(array, target, mid_idx + 1, right)
        else:
            return shifted_binary_search(array, target, left, mid_idx - 1)