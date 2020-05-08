import unittest

#Time Complexity O(N)
#Space Complexity O(N) since hash table might contain all n's
def is_edit_away(s1, s2):

    difference = abs(len(s1) - len(s2))

    if difference > 1:
        return False

    insertion_hash = {}

    for char in s1:
        if char in insertion_hash:
            insertion_hash[char] += 1
        else:
            insertion_hash[char] = 1
    
    for char in s2:
        if char in insertion_hash:
            insertion_hash[char] -= 1
        else:
            insertion_hash[char] = 1
    count = 0
    value_list = list(insertion_hash.values())

    for i in range(len(value_list)):
        if value_list[i] == abs(1):
            count += 1
    
    if difference == 1:
        return count <= 1
    else:
        return count <= 2


class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_edit_away('sale','sle'), True)

    def test_case_2(self):
        self.assertEqual(is_edit_away('sale','male'), True)

    def test_case_3(self):
        self.assertEqual(is_edit_away('sales','sale'), True)

    def test_case_4(self):
        self.assertEqual(is_edit_away('salesss','sale'), False)

    def test_case_5(self):
        self.assertEqual(is_edit_away('sales','1234'), False)

if __name__ == '__main__':
    unittest.main()