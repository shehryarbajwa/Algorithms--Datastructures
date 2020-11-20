def binary_range(array, target):
    final_range = [-1, -1]
    altered_binary_search(array, target, 0, len(array) - 1, True, final_range)
    altered_binary_search(array, target, 0, len(array) - 1, False, final_range)
    return final_range

def altered_binary_search(array, target, left, right, go_left, final_range):
	
    while left + 1 < right:

        mid = (left + right) // 2

        if array[mid] < target:
            left = mid
        elif array[mid] > target:
            right = mid
        else:
            if go_left:
                if mid == 0 or array[mid - 1] != target:
                    final_range[0] = mid
                    return
                else:
                    right = mid
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    final_range[1] = mid
                    return
                else:
                    left = mid
    if array[left] == target and array[left + 1] != target:
        final_range[0] = left
        final_range[1] = left
    if array[right] == target and array[right - 1] != target:
        final_range[0] = right
        final_range[1] = right
    if array[left] == target and array[right] == target:
        final_range[0] = left
        final_range[1] = right

print(binary_range([1,1], 1))