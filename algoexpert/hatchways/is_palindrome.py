
import unittest

def is_palindrome(string):
    i = 0

    while i < len(string) // 2:
        if string[i] != string[(i+1) * -1]:
            return False
        
        i += 1
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
    

if __name__ == '__main__':
    unittest.main()



