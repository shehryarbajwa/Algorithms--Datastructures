
# Time Complexity O(N)
# Space Complexity O(N)

import unittest

# Important to note that key represents the number of alphabets in ABC
# If it more than 26 then we have to reverse and start again at 0
# a represents 1 z 26
# chr(96 + value % 122) represents when we have a character that goes beyond 122 so we bring it back to 96 + 1,2,3 till 26
# That is how we get valuees within 96 - 122. From a - z



def ceaser(string, key):

    new_string = []
    key = key % 26

    for char in string:
        nlc = ord(char) + key
        if nlc <= 122:
            new_string.append(chr(nlc))
        else:
            new_string.append(chr(96 + nlc % 122))

    return ''.join(new_string)

    
print(ord('a')) print(ceaser('aby', 2))