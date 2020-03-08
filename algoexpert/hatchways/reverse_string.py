#reverse a given string. Do it in optimal time.

#Questions to ask. Is the string alphanumeric?
#Is the string only letters?
#is the string only numbers?
#Does the string have any punctuation?
#Does the string have any special characters?

# Reversing a string using a loop is bound to create a new string which will be the length of O(m + n)
# This is not necessarily optimal since strings in python are immutable. They are not changed and rather a new string is created.

# If we use string.slice()
# We can have a run time of O(size of slice)


import unittest

def reverse_string(string):

    i = len(string) - 1
    reverse = ''

    while i >= 0:
        reverse += string[i]
        i -= 1
    return reverse


def reverse_string_slice(string):
    #Slice has a syntax of slice[start:end:jump]
    #Slice has a run time of O(k) which is the size of the slice.
    #If we do it for string[4:8] the size is 4 so O(4)
    #The reason it is O(k) is because it traverses through not all element but can traverse through all elements.
    #in our case it does.
    #However in the case it traverses through 4:8, it only traverses through 4 indices and not the entire length of the array.
    

    return string[::-1]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    def test_case_2(self):
        self.assertEqual(reverse_string_slice('hello'), 'olleh')

if __name__ == '__main__':
    unittest.main()
