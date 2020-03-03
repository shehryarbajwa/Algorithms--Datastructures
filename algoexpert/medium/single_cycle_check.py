import unittest

#Time Complexity O(n)
#Space Complexity O(1)

def singleCyclearray(array):
    # Assume non dynamic array
    # Each number has to be visited exactly once
    # Example is [1, 2, 2, -1]

    numbersVisited = 0
    currentIndex = 0

    while numbersVisited < len(array):

        # If the number Visited is more than 0, and currentIndex == 0
        # This means we have visited some numbers but before finishing the entire list, we have returned to the first Element.
        # e.g [1,1,-2,2]
        # Here in this case we reach -2 and go back to 1 without reaching 2
        if numbersVisited > 0 and currentIndex == 0:
            return False

        numbersVisited += 1
        currentIndex = getNewIndex(array, currentIndex)

    return currentIndex == 0


def getNewIndex(array, currentIndex):
    # Jump is the index value of the array
    jump = array[currentIndex]
    indexAfterJump = (currentIndex + jump) % len(array)

    return indexAfterJump if indexAfterJump >= 0 else indexAfterJump + len(array)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(singleCyclearray([2, 2, -1]), True)
    
    def test_case_2(self):
        self.assertEqual(singleCyclearray([1, 2,2, -1]), True)
    
    def test_case_3(self):
        self.assertEqual(singleCyclearray([1, 2,3, -1]), False)

if __name__ == "__main__":
    unittest.main()