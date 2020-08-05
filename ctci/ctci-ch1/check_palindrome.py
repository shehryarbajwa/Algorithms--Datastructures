# abc cba palindrome
# aabc cbaa palindrome
# a fox is eating not a palindrome
# ignore whitespaces


def is_palindrome(string):
    if not len(string):
        return False

    if not string.isalnum():
        return False
    
    string.replace(' ','')

    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome('aabaa'))
print(is_palindrome('noon'))
print(is_palindrome('1234124'))
print(is_palindrome('aakhjsf'))