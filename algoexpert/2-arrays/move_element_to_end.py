import unittest

#Time Complexity O(N)
#Space Complexity O(1)

def move_element_to_end(array, target):
    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx < rightIdx:
        current_number = array[leftIdx]

        if current_number == target:
            swap(leftIdx, rightIdx, array)
            rightIdx -= 1
        else:
            leftIdx = leftIdx + 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(move_element_to_end([1,2,2,3,4,5], 2), [1,5,4,3,2,2])

    def test_case_2(self):
        self.assertEqual(move_element_to_end([1,2,2,3,4,5], 3), [1,2,2,5,4,3])



if __name__ == "__main__":
    unittest.main()