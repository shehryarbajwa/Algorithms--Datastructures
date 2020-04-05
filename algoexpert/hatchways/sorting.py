

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) -1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selection_sort(array):

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

def quick_sort(array):

    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, start, end):

    if start >= end:
        return


    pivot = start
    left_index = start + 1
    right_index = end

    while left_index <= right_index:
        if array[left_index] > array[pivot] and array[right_index] < array[pivot]:
            swap(left_index, right_index, array)

        if array[left_index] < array[pivot]:
            left_index += 1

        if array[right_index] > array[pivot]:
            right_index -= 1
    
    swap(pivot, right_index, array)
    left_subarray_length = right_index - 1 - start
    right_subarray_length = end - right_index + 1

    if left_subarray_length < right_subarray_length:
        quick_sort_helper(array, start, right_index - 1)
        quick_sort_helper(array, right_index + 1, end)
    else:
        quick_sort_helper(array, right_index + 1, end)
        quick_sort_helper(array, start, right_index - 1)

def merge_sort(array):

    merge_sort_helper(array)
    return array

def merge_sort_helper(array):

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    left_subarray = merge_sort_helper(left)
    right_subarray = merge_sort_helper(right)

    return merge(left_subarray, right_subarray)

def merge()
    
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(bubble_sort([9,8,3,4,6]))
print(selection_sort([9,8,3,4,6]))
print(quick_sort([9,8,3,4,6]))