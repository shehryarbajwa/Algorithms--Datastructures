import unittest

def is_unique(string):
    dups = {}

    for char in string:
        if char in dups:
            return False
        else:
            dups[char] = char

    return True

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_unique('shehryar'), False)

    def test_case_2(self):
        self.assertEqual(is_unique('abcdefghio'), True)

if __name__ == '__main__':
    unittest.main()