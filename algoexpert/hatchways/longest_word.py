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

def longest_word(sen):
    longest_word = []

    longest_word = sen.split(' ')

    result = [longest_word[0]]

    for element in longest_word[1:]:

        if len(element) == len(result):
            result[-1] = result

        if len(element) > len(result):
            result[-1] = element

    return result


def longest_word_punctuation(sen):
    for char in sen:
        if not char.isalnum():
            sen = sen.replace(char, ' ')
    print(sen)
    return max(sen.split(' '), key=len)




print(longest_word('i love dogs'))

print(longest_word_punctuation('fund&!! love dogs'))
        



