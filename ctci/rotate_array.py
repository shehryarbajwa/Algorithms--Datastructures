#Example

def rotate_array(array, k):
    count = 1

    while count <= k:
        last = array.pop()
        array.insert(0, last)
        count += 1
    return array

def rotate_array_reverse(array, k):
    k = k % len(array)

    reverse_array(array, 0, len(array) - 1)
    reverse_array(array, 0, k - 1)
    reverse_array(array, k, len(array) - 1)

    return array

def reverse_array(array, start, end):

    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1
    return array


print(rotate_array_reverse([-1,-100,3,99], 2))
