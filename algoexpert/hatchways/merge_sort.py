

def create_empty_array_size(size):

    return [None] * size

def merge_sort(array):

    if len(array) == 1:
        return array

    middle = 0
    if len(array) % 2 == 0:
        middle = (len(array) // 2)

    else:
        middle = (len(array) + 1) // 2

    left = array[:middle]
    right = array[middle:]

    left_subarray = merge_sort(left)
    right_subarray = merge_sort(right)

    return merge_array(left_subarray, right_subarray)

def merge_array(left, right):

    sorted_array = create_empty_array_size(len(left) + len(right))

    i = 0
    j = 0
    k = 0

    #One of the logics below finishes early depending on the items checked.
    #A dual conditional while loop runs till either one of them stops running but doesnt wait for both to end.


    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            sorted_array[k] = right[j]
            j += 1
            k += 1
        else:
            sorted_array[k] = left[i]
            i += 1
            k += 1
    
    while i < len(left):
        sorted_array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        sorted_array[k] = right[j]
        j += 1
        k += 1
    
    return sorted_array



print(merge_sort([1,4,9,2,3]))
    
    

    
