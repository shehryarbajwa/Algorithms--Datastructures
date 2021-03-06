def find_first(array, target):
    left = 0
    right = len(array) - 1

    while left + 1 < right:
        mid = (left + right) // 2

        if array[mid] == target:
            right = mid
        if array[mid] < target:
            left = mid
        else:
            right = mid
    
    if array[left] == target:
        return left
    if array[right] == target:
        return right
    return -1