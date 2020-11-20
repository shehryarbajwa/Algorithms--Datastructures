def find_last(array, target):
    left = 0
    right = len(array) - 1

    while left + 1 < right:

        mid = (left + right) // 2

        if array[mid] == target:
            left = mid
        elif array[mid] < target:
            left = mid
        else:
            right = mid
    
    if array[right] == target:
        return right
    if array[left] == target:
        return left
    return -1

print(find_last([2,8,8,8,8, 9, 12, 13, 13, 13, 13 ,16, 19], 13))