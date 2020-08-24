#permutation of a palindrome

def permutation_palindrome(string):
    string = string.replace(' ','')
    count = {}
    string = string.lower()

    for i in range(len(string)):
        if string[i] in count:
            count[string[i]] -= 1
        else:
            count[string[i]] = 1
    
    for value in count.values():
        if value > 1:
            return False
    return True

print(permutation_palindrome('Tact coa'))