#s='1234'
#Time Complexity O(N)
#Space Complexity O(9)
def only_digits(string):
    digits = set()
    for i in range(0, 10):
        digits.add(i)

    for i in range(len(string)):
        if (ord(string[i]) - ord('0')) not in digits:
            return False
    return True

print(only_digits('aaaaa'))