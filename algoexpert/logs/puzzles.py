
#Time Complexity O(N)
#Space Complexity O(1)
import unittest

def countHoles(number):
    num_sum = 0

    for character in str(number):
        print(character)
        if character in ['0','4','6','9']:
            num_sum += 1
        elif character == '8':
            num_sum += 2
        else:
            num_sum = num_sum

    return num_sum

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(countHoles(1428), 3)

    def test_case_2(self):
        self.assertEqual(countHoles(469), 3)

    def test_case_3(self):
        self.assertEqual(countHoles(12357), 0)

    def test_case_4(self):
        self.assertEqual(countHoles(444666999), 9)

    def test_case_5(self):
        self.assertEqual(countHoles(88888), 10)

if __name__ == '__main__':
    unittest.main()
