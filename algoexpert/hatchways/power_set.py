# We are given a list [1,2,3] and we are asked to provide all possible subsets

# A subset is [1],[2],[3],[],[1,2],[1,3],[1,2,3]
# It should be asked that subsets are not in same order. [2,1] is same as [1,2] and both need not be included.

import unittest

def subset(array):

    subsets = [[]]

    i = 0

    while i < len(array):
        for j in range(len(subsets)):
            current_subset = subsets[j]
            subsets.append(current_subset + [array[i]])
        i += 1
    return subsets


class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(subset([1,2,3]),[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

if __name__ == '__main__':
    unittest.main()