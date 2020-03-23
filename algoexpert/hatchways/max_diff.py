# Maximum difference between two elements such that larger element appears after the smaller number

import unittest
# Input arr = 

arr = [1,2,3,4,4,5,6,7,12]

#Time Complexity O(N^2) since we have to traverse the entire array once.
#Then we have to traverse the entire array again
#Space Complexity O(1) since we are doing all operations in order.

def max_diff(array):
    #It runs like this. First the outerloop runs.
    #we start at index 0 so with value 1.
    #Then the inner loop runs from 2 - 12.
    #At each iteration, we check if difference is greater than max_diff we setup initially
    #Then we start with the next number 2 and traverse till 12.

    max_diff = array[1] - array[0]
    
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] - array[i] > max_diff:
                max_diff = array[j] - array[i]
    return max_diff

#Efficient Solution
#Time Complexity O(N)
# Space Complexity O(1)

def max_difference(array):
    max_diff = array[1] - array[0]
    min_element = array[0]

    for i in range(len(array)):
        #denom
        if array[i] - min_element > max_diff:
            max_diff = array[i] - min_element
        
        if array[i] < min_element:
            min_element = array[i]

    return max_diff

class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_difference([1, 2, 3,4,5,6]), 5)

    def test_case_2(self):
        self.assertEqual(max_difference([1, 2, 4,4,5,12]), 11)

    def test_case_3(self):
        self.assertEqual(max_difference([1, 2, 4,4,5,1100]), 1099)


if __name__ == '__main__':
    unittest.main()
