
def subset(array):
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            new_subset = subsets[i] + [element]
            subsets.append(new_subset)

    return subsets


def palindrome(string):
    left_index = 0
    right_index = len(string) - 1

    while left_index < right_index:
        if string[left_index] != string[right_index]:
            return False
        if len(string) % 2 != 0:
            return False
        left_index += 1
        right_index -= 1
    return True

def bubble_sort(array):

    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                swap(j, j+ 1, array)

    return array

def insertion_sort(array):

    for i in range(1,len(array)):
        j = i

        while j > 0 and array[j] < array[j - 1]:
            swap(j, j-1, array)
            j -= 1

    return array

def quick_sort(array):
    if not len(array):
        return []
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, start, end):

    #Base case is when the right side crosses over the left side
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

    #Recursion step

    left_subarray_length = right_index - 1 - start
    right_subarray_length = end - right_index + 1

    if left_subarray_length < right_subarray_length:
        quick_sort_helper(array, start, right_index - 1)
        quick_sort_helper(array, right_index + 1, end)
    else:
        quick_sort_helper(array, right_index + 1, end)
        quick_sort_helper(array, start, right_index - 1)


def merge_sort(array):

    if len(array) == 1:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    left_subarray = merge_sort(left)
    right_subarray = merge_sort(right)

    return merge_subarrays(left_subarray, right_subarray)

def merge_subarrays(left_subarray, right_subarray):

    dynamic_array = [None] * (len(left_subarray) + len(right_subarray))

    i = j = k = 0

    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] < right_subarray[j]:
            dynamic_array[k] = left_subarray[i]
            i += 1
            k += 1
        else:
            dynamic_array[k] = right_subarray[j]
            j += 1
            k += 1
        
    while i < len(left_subarray):
        dynamic_array[k] = left_subarray[i]
        i += 1
        k += 1

    while j < len(right_subarray):
        dynamic_array[k] = right_subarray[j]
        j += 1
        k += 1
    
    return dynamic_array

def binary_search(array, target):

    return binary_search_helper(array, 0, len(array) - 1, target)

def binary_search_helper(array, start, end, target):

    if start >= end:
        return -1

    middle = (start + end) // 2
    middle_element = array[middle]

    if target == middle_element:
        return middle
    elif target < middle_element:
        return binary_search_helper(array, start, middle - 1, target)
    else:
        return binary_search_helper(array, middle + 1, end, target)
        

def kth_largest_element_quick_select(array, k):
    if not len(array):
        return []
    position = len(array) - k
    return quick_select_helper(array,0, len(array) - 1, position)
    

def permutations(array):
    if len(array) == 0:
        return []

    final_permutations = []
    permutations_helper(array, [], final_permutations)
    return final_permutations

def permutations_helper(array, temporary_permutation, final_permutations):

    if not len(array):
        final_permutations.append(temporary_permutation)
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i+1:]
            current_permutation = temporary_permutation + [array[i]]
            permutations_helper(new_array, current_permutation, final_permutations)

def quick_select_helper(array, start, end, position):

    while True:
        pivot = start
        left = start + 1
        right = end

        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(left, right, array)

            if array[left] < array[pivot]:
                left += 1

            if array[right] > array[pivot]:
                right -= 1

        swap(pivot, right, array)

        if right == position:
            return array[right]

        elif right < position:
            start = right + 1
        else:
            end = right - 1

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(bubble_sort([4,9,1,3,2]))
print(insertion_sort([4,9,1,3,2]))
print(quick_sort([4,9,1,3,2]))
print(merge_sort([4,9,1,3,2]))
print(kth_largest_element_quick_select([4,9,1,3,2],1))
print(binary_search([1,2,3,9,5],9))
print(permutations([1,2,3]))