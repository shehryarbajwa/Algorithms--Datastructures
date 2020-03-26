

def bubble_sort(array):

    if len(array) == 1:
        return array
        
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def insertion_sort(array):

    if len(array) == 1:
        return array
    
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

def quick_sort(array):
    quicksorthelper(array, 0, len(array) - 1)
    return array

def quicksorthelper(array, start, end):

    #base case
    #If array is empty or 1 element

    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]

        if array[left] < array[pivot]:
            left += 1

        if array[right] > array[pivot]:
            right -= 1

    swap(pivot, right, array)
    left_length = right - 1 - start
    right_length = end - right + 1

    if left_length < right_length:
        quicksorthelper(array, start, right - 1)
        quicksorthelper(array, right + 1, end)
    else:
        quicksorthelper(array, right + 1, end)
        quicksorthelper(array, start, right - 1)

    
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


