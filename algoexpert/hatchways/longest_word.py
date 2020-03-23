#We are being asked to return the largest word in the string. If there are two or more words,
#That are the same length, return the first word from the string with that length.
#Ignore punctuation and assume sen will not be empty


# Example "fun&!! time"
# Output 'time'

# Input "I love dogs"
# Output "love"

# The question to ask is are there just letters in the input string?
# How to deal with punctuation? ignore them


# Naive approach will be to traverse the entire string. and compare the first string element with the reamining elements.

import unittest

#Time Complexity O(n^2) complexity since we iterate over the input string.
#Then replace is a O(N) time complexity in avg time and O(N * N) in worst time since we might have to replace it with something that is equally time consuming

#Space Complexity is O(1) since we are doing in order replacement and not using a new data structure to hold the resultant string.


def longest_word_punctuation(string):
    for word in string:
        #If character is not alphanumeric
        if word.isalnum() is not True:
            #replace the character with a space
            string = string.replace(word, ' ')
    #Return the max of sen.split(' ') by key = length and since it is a return, 
    # the first value with the longest string will be returned.
    #Max will scan the entire input string and return the first occureence of the longest string.
    return max(string.split(' '), key=len)

# print(longest_word('i love dogs'))

class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(longest_word_punctuation('I love dogs'), 'love')

    def test_case_2(self):
        self.assertEqual(longest_word_punctuation('I love doggies'), 'doggies')

    def test_case_3(self):
        self.assertEqual(longest_word_punctuation('I love!!! doggies'), 'doggies')

    def test_case_4(self):
        self.assertEqual(longest_word_punctuation('I admiree!gee doggies'), 'admiree')

    def test_case_5(self):
        self.assertEqual(longest_word_punctuation('hello and nicer'), 'hello')

    



if __name__ == '__main__':
    unittest.main()
        



