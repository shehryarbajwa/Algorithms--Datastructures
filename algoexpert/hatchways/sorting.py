

def insertion_sort(array):

    for i in range(1,len(array)):
        j = i

        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

def palindrome(string):

    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] != string[right]:
            return False

        if len(string) % 2 != 0:
            return False

        left += 1
        right -= 1
    return True

def bubble_sort(array):

    for i in range(len(array)):
        for j in range(len(array) - 1 -i):
            if array[j] > array[j + 1]:
                swap(j,j + 1,array)
    return array

def merge_sort(array):

    if len(array) == 1:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    left_subarray = merge_sort(left)
    right_subarray = merge_sort(right)

    return merge(left_subarray, right_subarray)

def merge(left, right):

    dynamic_array = [None] * (len(left) + len(right))
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            dynamic_array[k] = right[j]
            j += 1
            k += 1
        else:
            dynamic_array[k] = left[i]
            i += 1
            k += 1

    while i < len(left):
        dynamic_array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        dynamic_array[k] = right[j]
        j += 1
        k += 1

    return dynamic_array


def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, start, end):

    if start >= end:
        return

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

    swap(pivot, right , array)

    left_length = right - 1 - start
    right_length = end - right + 1

    if left_length < right_length:
        quick_sort_helper(array, start, right - 1)
        quick_sort_helper(array, right + 1, end)

    else:
        quick_sort_helper(array, right + 1 , end)
        quick_sort_helper(array, start, right - 1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def kth_smallest_element(array,k):
    array.sort()
    position = k - 1

    return array[position]

def kth_largest_element(array,k):

    position = len(array) - k

    return quick_select(array, 0, len(array) - 1,position)

def quick_select(array, start, end, position):

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

        swap(pivot, right , array)

        if right == position:
            return array[right]
        elif right < position:
            #How will we change pivot if we change the values of just left and right.
            #If we change start and end, we can re-assign values to all three variables.
            #vs going and changing the pivot and 
            start = right + 1
        else:
            end = right - 1
    



print(palindrome('abba'))
print(palindrome('absba'))
print(palindrome('palind'))
print(bubble_sort([4,9,18,1,2]))
print(quick_sort([4,9,18,1,2]))
print(merge_sort([4,9,18,1,2]))
print(insertion_sort([4,9,18,1,2]))
print(kth_largest_element([4,9,18,1,2], 2))

