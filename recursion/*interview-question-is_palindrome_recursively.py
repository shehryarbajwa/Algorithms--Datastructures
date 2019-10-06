# A palindrome is a word that is the reverse of itself—that is, it is the same word when read forwards and backwards.

# For example:

# "madam" is a palindrome
# "abba" is a palindrome
# "cat" is not
# "a" is a trivial case of a palindrome
# The goal of this exercise is to use recursion to write a function is_palindrome that takes a string as input and checks whether that string is a palindrome. 


def is_palindrome(input_string):

    if input_string[0] == input_string[-1]:
        return True
    elif len(input_string) == 1:
            return True
    elif len(input_string) >= 1 and input_string[0] is not input_string[-1]:
        return False
    else:
        first_char = input_string[0]
        last_char = input_string[-1]
        sub_string = input_string[1:-1]
        ispalindrome = is_palindrome(sub_string)
        

print(is_palindrome('Udacity'))

# So we need to think this through with what a palindrome is. Each starting letter is equal to the last letter in case
# the length of the palindrome is even
# In case the length of the palindrome is odd, the final length of the input will be 1

#   Example of odd palindrome
#   madam
#   ada
#   d
#   Since the length of the final string is 1, we call it a palindrome

#   Example of odd palindrome
#   racecar
#   aceca
#   cec
#   e
#   Since the length of the final string is 1, we call it a palindrome

#   Example of even palindrome
#   abba
#   bb
#   Since element at 1 and -1 are the same, we call it True

#   Example of even palindrome
#   abccba
#   bccb
#   cc
#   Since the element at 1 and -1 are the same, we call it True

def _is_palindrome(input):

    if len(input) <= 1:
        return True
    else:
        first_character = input[0]
        last_character = input[-1]
        sub_input = input[1:-1]
        return (first_character == last_character) and _is_palindrome(sub_input)

#Lets take two examples one even and odd and run it via this algorithm

# Example 1:
# madam
# Since len is > 1, we continue
# First_character is m
# Last character is m
# sub_input is ada
# we return first_character = last_character which is True and then again run the _is_palindrome function
# Now first_character is a
# Last character is a
# sub_input = d
# first_character and last_character are True but we run _is_palindrome again
# Now the length is <= 1, so we return True
# We returned True and True
# If it is False and True, it will return False

# Example 2:
# abba
# Since len is > 1, we continue
# First_character is a
# Last character is a
# sub_input is bb
# we return first_character = last_character which is True and then again run the _is_palindrome function
# Now first_character is b
# Last character is b
# sub_input = 0
# first_character and last_character are True but we run _is_palindrome again
# Now the length is <= 1, so we return True
# We returned True and True
# In this case it is True and True which leads to True
# If it is False and True, it will return False

# Example 3:
# Not a palindrome
# abcdba
# Since len is > 1, we continue
# First_character is a
# Last character is a
# sub_input is bcdb
# return True and _is_palindrome again
# first_character is now b
# last_character is b again
# sub_input = cd
# run is_palindrome again
# first_character is c
# last_character is d
# sub_string is None
# return False and return the value without proceeding further
# and means both conditions are True to be True
# FYI [] still has length property accessible on it and returns 0

#It is most optimal if recursion has one base case

print(_is_palindrome('abba'))
print(_is_palindrome('boby'))