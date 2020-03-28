

import unittest

def create_dynamic_array(size):

    return [None] * size


#Time Complexity 
# Average: O(nlogn)
# Worst : O(nlogn)
# Best: O(Nlogn)
#Space Complexity O(N) for using a dynamic array
def merge_sort(array):

    if len(array) == 0:
        return []

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

    sorted_array = create_dynamic_array(len(left) + len(right))

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


class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(merge_sort([1,4,9,2,3]), [1,2,3,4,9])

    def test_case_2(self):
        self.assertEqual(merge_sort([1,4,19,32,3]), [1,3,4,19, 32])

    def test_case_3(self):
        self.assertEqual(merge_sort([]), [])

    def test_case_4(self):
        self.assertEqual(merge_sort([1,4,9,11]), [1,4,9,11])


if __name__ == '__main__':
    unittest.main()


    
    

    
