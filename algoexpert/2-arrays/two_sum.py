
import unittest

#Time Complexity O(N)
# Space Complexity O(N)
def two_sum(array, target):

    sum_map = {}

    for num in array:
        if target - num in sum_map:
            return [target - num, num]
        else:
            sum_map[num] = True
    return []

class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(two_sum([1,2,3,4,5,6,7,8,9,10], 10), [4,6])

    def test_case_2(self):
        self.assertEqual(two_sum([1,2,3,4,5,6,7,8,9,10], 5), [2,3])


if __name__ == "__main__":
    unittest.main()


