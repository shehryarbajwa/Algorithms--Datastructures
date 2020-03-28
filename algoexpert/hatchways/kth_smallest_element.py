#arr= [7, 10, 4, 3, 20, 15]

import unittest
#To find the 2nd smallest element
import random
#Time Complexity O(nlogn) since we sort the array first.
#[15,4,1,9,18] -> [1,4,9,15,18]
# smallest is 1, second smallest is 4 and so on.
# we can see that since it is sorted, it starts from smallest to largest.
# To access the smallest, it is at index 0 of array.
# We are given k
# We can see that when k is 1, for first smallest number we need to return array at 0.
# We can see that when k is 2, for second smallest number we need to return array at 1.
# Space Complexity O(1)
def kth_smallest_element(array, k):

    array.sort()

    smallest = array[k - 1]

    return smallest

#Time Complexity O(nlogn) since we sort the array first.
#Space Complexity O(1)
#[15,4,1,9,18] -> [1,4,9,15,18]
#When this array gets sorted, we can see the largest numbers are at the end.
#If we have to return the 1st largest number, we see it is the last element of the array
#If we have to return the 2nd largest number, we see it is the second last element of the array

#We are given k
#If k is 1, we need to return the last number.
#Last number can be returned as -1 or len(string) - 1
#If we want -1, we can multiply k with -1
#If we want len(string), we can subtract it from len(string) - k.


def kth_largest_element(array, k):
    """
        :type array: List[int]
        :type k: int
    """

    array.sort()

    largest = array[len(array) - k]

    return largest

def kth_largest_element_quick_select(array, k):

    """
        :type array: List[int]
        :type k: int
    """
    #Position is k - 1. If we have to find the 2nd smallest element, we need the array at index 1
    position = k - 1
    return quick_select(array, 0, len(array) - 1, position)

def quick_select(array, start, end, position):


    pivot = start
    left = start + 1
    right = end

    while True:

        #Base case

        if start > end:
            break

        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(left, right, array)

            if array[left] < array[pivot]:
                left += 1

            if array[right] > array[pivot]:
                right -= 1

        swap(pivot, right, array)

        #Pivot is now at right index after swap
        if right == position:
            return array[right]

        #If pivot is < position
        #We update the pivot, and instead of calling a recursive algorithm, we keep running this one
        #This is itself a recursive algorithm since it will keep on looping until it finds what it is looking for
        #By updating the start, once the first iteration ends, the array has skipped the left part, and now it starts after the pivot.

        elif right < position:
            start = right + 1
        #If it is smaller than pivot, we have skipped the right part and change the end to be one before pivot.
        else:
            end = right - 1

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    unittest.main()


class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(kth_largest_element_quick_select([4,1,9,12], 2) , 4)