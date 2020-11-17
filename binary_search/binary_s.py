

def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left + 1 < right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid
        else:
            right = mid
    if array[left] == target:
        return left
    if array[right] == target:
        return right
    return -1

print(binary_search([1,2,2,4,5,5,8], 8))