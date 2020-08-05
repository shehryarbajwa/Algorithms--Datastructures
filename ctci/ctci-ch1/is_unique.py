# aabcdef 
# abcdefgh
# is_unique(aabcdef) -> not true

def is_unique(string):
    if not len(string):
        return False

    count = {}
    for char in string:
        if char in count:
            return False
        else:
            count[char] = 1
    return True

print(is_unique('abcdefgh'))