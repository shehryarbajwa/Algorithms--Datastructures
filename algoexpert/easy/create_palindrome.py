
#Time Complexity O(N^2)
#Space Complexity O(N) length of our input string. 
#Because we are creating a new string of the same length as our input string

# It is O(N^2) because we iterate over the new string variable and add a new string to it each time.
# String concatenation works in O(N) time in programming languages

#Why? Strings are immutable and can't be changed in place. 
#To alter one, a new representation needs to be created (a concatenation of the two).
def isPalindrome(string):

    new_string = ''

    for i in reversed(range(len(string))):
        new_string += string[i]

    return new_string == string

#Time Complexity O(N) since append is a constant time function
#Space Complexity O(N) since new_string is the same length as of our original string
    
def isPalindrome_(string):

    new_string = []

    for i in reversed(range(len(string))):
        new_string.append(string[i])

    return "".join(new_string) == string

#Solve recursively

def isPalindromeRecursion(string, i=0):
    j = len(string) - i - 1

    #Till we reach the middle element
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    
    return isPalindromeRecursion(string, i+1)

print(isPalindromeRecursion('abba'))
# Iteratively using pointers
# Here Time Complexity is O(N)
# Space Complexity is O(1) since we are not storing anything just using pointers
# The most optimal solution is this

def isPalindrome__(string):
    leftIndex = 0
    rightIdx = len(string) - 1

    while leftIndex < rightIdx:
        if string[leftIndex] != string[rightIdx]:
            return False
        leftIndex += 1
        rightIdx -= 1
    
    return True