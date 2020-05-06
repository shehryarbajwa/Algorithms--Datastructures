import unittest

#Time Complexity O(N log n)
#Space Complexity O(1)

def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = sorted(s1, key=lambda x: x)
    s2 = sorted(s2, key=lambda x: x)

    if s1 == s2:
        return True
    else:
        return False

#Time Complexity O(N)
#Space Complexity O(N)
def is_permutation_constant(s1, s2):
    if len(s1) != len(s2):
        return False

    common = {}
    for char in s1:
        if char in common:
            common[char] += 1
        else:
            common[char] = 1
    
    for char in s2:
        if char in common:
            common[char] -= 1
            continue
        else:
            return False
    return True
    

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_permutation_constant('shehryar', 'hehryars'), True)

    def test_case_2(self):
        self.assertEqual(is_permutation_constant('shehryar', 'shehryar   '), False)

    def test_case_3(self):
        self.assertEqual(is_permutation_constant('abc', 'cab'),True)

    def test_case_4(self):
        self.assertEqual(is_permutation_constant('abc', 'cat'), False)


if __name__ == '__main__':
    unittest.main()