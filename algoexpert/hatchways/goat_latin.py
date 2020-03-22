# Three rules
# If word begins with a vowel, append ma to the end of the word
# If word begins with a consonant, remove the first letter and append it to the end.
# Add one letter a to the end of each word per its word index in the sentence. If the word is the first word, add a. If the word is the second word, add aa. If the word is the third word, add aaa

# Steps to go about it. 

# Slice doesnt work on strings. So donot waste time.

import unittest

def goat_latin(string):

    sentence_array = string.split(' ')
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    i = 0
    counter = 1

    new_str = ''

    while i < len(sentence_array):
        if sentence_array[i][0] in vowels:
            new_str += sentence_array[i] + 'ma' + 'a' * counter + ' ' 
            i += 1

        elif sentence_array[i][0] not in vowels:
            first_letter = sentence_array[i][0]
            new_str += sentence_array[i][1:] + first_letter + 'ma' + 'a' * counter + ' ' 
            i += 1

        counter += 1

    return new_str

class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(goat_latin('I Speak Goat Latin'), 'Imaa peakSmaaa oatGmaaaa atinLmaaaaa ')

    def test_case_2(self):
        self.assertEqual(goat_latin('The quick brown fox jumped over the lazy dog'), 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa ')

    def test_case_3(self):
        self.assertEqual(goat_latin('Coronavirus is a pandemic'), 'oronavirusCmaa ismaaa amaaaa andemicpmaaaaa ')

if __name__ == '__main__':
    unittest.main()




