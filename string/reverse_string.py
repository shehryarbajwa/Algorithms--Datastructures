"""
Reverse a given string
Algorithm: Strings training
"""

def reverse(our_string):
    new_string = ' '

    for i in range(len(our_string)):
        new_string += our_string[(len(our_string)-1)-i]
        
    return new_string

print(reverse("abc"))