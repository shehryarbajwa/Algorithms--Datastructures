import unittest
def product_sum(array, depth=1):
    sum = 0
    
    for char in array:
        if type(char) == list:
            temp_sum = product_sum(char, depth + 1)
            sum += temp_sum
        else:
            sum += char
    return sum * depth


class test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(product_sum([[[5]]]), 30)

if __name__ == '__main__':
    unittest.main()

    
