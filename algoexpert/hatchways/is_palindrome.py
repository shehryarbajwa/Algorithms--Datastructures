
import unittest

# Clarifying questions.

# Does the input string contain strings only or numbers?
# Does the input contain lowercase or uppercase?
# Does it contain any punctuation?
# What are the tradeoffs to compare each element with the last element?

def is_palindrome(string):
    i = 0

    while i < len(string) // 2:
        if string[i] != string[(i+1) * -1]:
            return False
        
        i += 1
    return True

def is_palindrome_1(string):

    left_index = 0
    right_index = len(string) - 1

    while left_index <= right_index:
        if string[left_index] != string[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_palindrome('Udacity'), False)

    def test_case_2(self):
        self.assertEqual(is_palindrome('abba'),True)
    
    def test_case_3(self):
        self.assertEqual(is_palindrome('aba'), True)

    def test_case_4(self):
        self.assertEqual(is_palindrome('baba'), False)

    def test_case_5(self):
        self.assertEqual(is_palindrome_1('baba'), False)

    def test_case_6(self):
        self.assertEqual(is_palindrome_1('aba'), True)
    

if __name__ == '__main__':
    unittest.main()



