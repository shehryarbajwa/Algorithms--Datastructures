
#Insertion sort works by using the first element of the array as a sorted array.
#We then traverse through the remaining elements one by one.
#The outer loop moves from left to right.

#If each element is less than the previous element, we keep swapping.
#The inner loop keeps comparing elements and keeps swapping if they are smaller.
#Each time, we decreement the loop and make sure that j is > 0.
#During the last iteration of this loop, j - 1 is changed and j becomes 0 and the loop stops.

#The idea is one loop for moving forwards.
#Another loop for moving backwards and comparison.
#The first element to be a sorted array

import unittest

def insertion_sort(array):

    for i in range(1, len(array)):
        j = i

        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(insertion_sort([1,2,9,11,3,4]), [1,2,3,4,9,11])

    def test_case_2(self):
        self.assertEqual(insertion_sort([1,9,11,13,4,2]), [1,2,4,9,11,13])


if __name__ == '__main__':
    unittest.main()

