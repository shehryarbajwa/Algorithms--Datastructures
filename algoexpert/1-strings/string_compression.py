
#Time Complexity O(N)
#Space Complexity O(N)

import unittest

def string_compression(string):
    walker = 0
    runner = 0

    while runner < len(string):
        string[walker] = string[runner]
        count = 1

        while runner + 1 < len(string) and string[runner] == string[runner + 1]:
            runner += 1
            count += 1
        
        if count > 1:
            for c in string(count):
                


class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(string_compression('aabcccccaaa'),'a2b1c5a3')
    def test_case_2(self):
        self.assertEqual(string_compression('aaaallimo'),'a4l2i1m1o1')


if __name__ == '__main__':
    unittest.main()
    