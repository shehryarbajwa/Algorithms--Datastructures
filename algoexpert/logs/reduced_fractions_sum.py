import fractions
from fractions import Fraction

import unittest

#Time Complexity O(N)
#Space Complexity O(N)

def reduced_fractions_sum(fractions):

    array = []

    for fraction in fractions:
        split_fraction = fraction.split('+')
        first_addition = split_fraction[0]
        second_addition = split_fraction[1]
        first_fraction = Fraction(first_addition)
        second_fraction = Fraction(second_addition)
        sum_fraction = first_fraction + second_fraction
        array.append(str(sum_fraction.numerator) + '/' + str(sum_fraction.denominator))
    
    return array

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(reduced_fractions_sum(['12/20 + 20/24']), ['43/30'])
    
    def test_case_2(self):
        self.assertEqual(reduced_fractions_sum(['10/10 + 20/10']), ['3/1'])

    def test_case_3(self):
        self.assertEqual(reduced_fractions_sum(['20/20 + 43/300', '1/19 + 191/143']), ['343/300', '3772/2717'])


if __name__ == '__main__':
    unittest.main()

