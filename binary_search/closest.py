def binary_search_closest(array, target):
    left = 0
    right = len(array) - 1

    while left + 1 < right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid
        else:
            right = mid
    
    if abs(target - array[left]) <= abs(target - array[right]):
        return left
    else:
        return right
    


print(binary_search_closest([1,2,3,6,7],0))