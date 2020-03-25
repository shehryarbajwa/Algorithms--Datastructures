import unittest

def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, start_index, end_index):

    #When the array has no elements
    if start_index >= end_index:
        return

    pivot = start_index
    left_pointer = start_index + 1
    right_pointer = end_index

    #Remember, to break the loop when left pointer is greater than right pointer
    while left_pointer <= right_pointer:
        #First check to see if both values can be swapped before moving to increment or decrement
        if array[left_pointer] > array[pivot] and array[right_pointer] < array[pivot]:
            swap(left_pointer, right_pointer, array)

        if array[left_pointer] <= array[pivot]:
            left_pointer += 1

        if array[right_pointer] >= array[pivot]:
            right_pointer -= 1

        # if array[left_pointer] > array[pivot]:
        #     #Do nothing

        # if array[right_pointer] < array[pivot]:
        #     #Do nothing

    #Swap pivot with right pointer
    swap(pivot, right_pointer, array)
    leftsubarray_length = (right_pointer - 1 - start_index + 1)
    rightsubarray_length = (end_index - right_pointer + 1 + 1)

    leftSubarrayissmaller = leftsubarray_length < rightsubarray_length

    if leftSubarrayissmaller:
        quickSortHelper(array, start_index, right_pointer - 1)
        quickSortHelper(array, right_pointer + 1, end_index)
    else:
        quickSortHelper(array, right_pointer + 1, end_index)
        quickSortHelper(array, start_index, right_pointer - 1)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(quickSort([1,4,9,8,3,1]), [1,1,3,4,8,9])

    def test_case_2(self):
        self.assertEqual(quickSort([1,4,99,88,33,1,4,0,3]), [0,1,1,3,4,4,33,88,99])

    

if __name__ == '__main__':
    unittest.main()