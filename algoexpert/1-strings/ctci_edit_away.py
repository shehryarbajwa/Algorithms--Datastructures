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
if len(s) == len(t):
            return self.one_edit_replace(s, t)
        elif len(s) + 1 == len(t):
            return self.one_removal(s, t)
        elif len(s) - 1 == len(t):
            return self.one_removal(t, s)
        else:
            return False
        
    def one_edit_replace(self, s, t):
        found_difference = False
        
        for i in range(len(s)):
            if s[i] != t[i]:
                #If we found difference the second time in our loop, we can exit
                if found_difference:
                    return False
                found_difference = True
        return True
    
    def one_removal(self, s , t):
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if i != j:
                    return False
                j += 1
            else:
                i += 1
                j += 1
        return True
if __name__ == '__main__':
    unittest.main()