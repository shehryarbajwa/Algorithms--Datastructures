import unittest


#Time Complexity
#Best case O(N) times if the array is already sorted.
#Average Case O(N^2) times since we iterate over the array, then compare each element in the array
#Worst case O(N^2) times

#Space Complexity is O(1) space since we do things in order.

def bubbleSort(array):

    #The outerloop runs for each element in the array N times.

    for i in range(len(array)):

        #Each time we have run an iteration of bubble sort, we are moving backwards by the index of outerloop
        #This is because at 0, we loop over all elements.
        #At 1, we skip the last element since it is sorted.
        #At 2, we skip the last 2 elements since they are sorted
        #That is why we subtract i.


        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

print(bubbleSort([1,9,14,2,3]))

class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(bubbleSort([1,3,4,3,9]), [1,3,3,4,9])

    def test_case_2(self):
        self.assertEqual(bubbleSort([1,3,4,3,9,6]), [1,3,3,4,6,9])


if __name__ == "__main__":
    unittest.main()