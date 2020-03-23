import unittest
# Binary search is an efficient algorithm for finding an item from a sorted list of items

# Given an array [1,2,5,9,11,19,24,36] find the index position of 11.

#Naive solution is O(N) time since we scan the entire array and return the array index of the target.
#Space complexity is O(1) since we are doing it in-order
def naive_binary_search(array, target):
    i = 0
    while i < len(array):
        if(array[i] == target):
            return i
        else:
            i += 1

#Recursive Time Complexity O(logn)
#Space Complexity O(logn) for space occupied in call stack.
def binary_search_recursive(array, target):
    return binary_search_helper(array, target, 0, len(array) - 1)

def binary_search_helper(array, target, left, right):

    #Left pointer gets bigger when we have scanned the entire array and found no match.
    #At each recursive iteration on the right we are making left scan the array and it not found move to the right.
    #At each recursive iteration on the left we are making right go left until it moves out of bounds.

    #To the right, left moves out of bounds.
    #To the left, right moves out of bounds

    if left > right:
        return -1

    middle_index = (left + right) // 2
    middle_element = array[middle_index]

    if target == middle_element:
        return middle_index

    if target < middle_element:
        return binary_search_helper(array, target, left, middle_index - 1)

    if target > middle_element:
        return binary_search_helper(array, target, middle_index + 1, right)

def binary_search_iterative(array, target):
    return binary_search_helper_iterative(array, target, 0 , len(array) - 1)

def binary_search_helper_iterative(array, target, left, right):

    #While the left pointer is not greater than right.
    while left <= right:

        middle_index = (left + right) // 2
        middle_element = array[middle_index]

        if target == middle_element:
            return middle_index
        elif target < middle_element:
            right = middle_index - 1
        else:
            left = middle_index + 1

    return -1




class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binary_search_recursive([1,2,3,4,5,6], 2), 1)

    def test_case_2(self):
        self.assertEqual(binary_search_recursive([1,2,3,4,5,6,7,8], 3), 2)

    def test_case_3(self):
        self.assertEqual(binary_search_iterative([1,2,3,4,5,6,7,8], 3), 2)

    def test_case_4(self):
        self.assertEqual(binary_search_iterative([1,2,3,4,5,6,7,8], 6), 5)



if __name__ == '__main__':
    unittest.main()

