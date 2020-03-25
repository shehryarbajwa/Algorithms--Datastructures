# Given an array check if the sum of the adjacent elements equals to a target and return the index values in an array

import unittest

def target_sum(array, target):
    empty = []

    for i in range(len(array) - 1):
        if array[i] + array[i + 1] == target:
            empty.append([array[i], array[i + 1]])
        else:
            continue

    return empty


class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(target_sum([1,2,3,1,4], 5), [[2,3],[1,4]])

    def test_case_2(self):
        self.assertEqual(target_sum([1,2,3,3,4], 6), [[3,3]])

    def test_case_3(self):
        self.assertEqual(target_sum([1,2,3], 4), [])

if __name__ == "__main__":
    unittest.main()
