
# Time Complexity O(N)
# Space Complexity O(N)

import unittest

# Important to note that key represents the number of alphabets in ABC
# If it more than 26 then we have to reverse and start again at 0
# a represents 1 z 26
# chr(96 + value % 122) represents when we have a character that goes beyond 122 so we bring it back to 96 + 1,2,3 till 26
# That is how we get valuees within 96 - 122. From a - z




def caesarCipherEncrypt(string, key):

    ord_array = []
    new_string = []

    key = key % 26

    for i in range(len(string)):
        ord_array.append(ord(string[i]) + key)

    for value in ord_array:
        if value <= 122:
            new_string.append(chr(value))
        else:
            new_string.append(chr(96 + value % 122))

    return "".join(new_string)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesarCipherEncrypt('abc', 54), 'cde')


if __name__ == '__main__':
    unittest.main()
