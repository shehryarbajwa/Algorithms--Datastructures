import unittest


def find_minimum_rotated_array(array):
    point = find_inflection_point(array)
    if point == len(array) - 1:
        return array[0]
    return min(array[0], array[point + 1])

#O(N) operation
def find_inflection_point(array):

    left = 0
    right = len(array) - 1

    while left + 1 < right:
        mid = (left + right) // 2

        if array[mid] > array[mid + 1]:
            return mid

        if array[mid] > array[left]:
            left = mid
        else:
            right = mid
    
    if array[left] > array[left + 1]:
        return left
    if array[right] > array[right - 1]:
        return right

print(find_minimum_rotated_array([2,1]))