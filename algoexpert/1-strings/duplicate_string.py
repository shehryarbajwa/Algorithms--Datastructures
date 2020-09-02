

def duplicates(string):
    count = {}
    dups = []

    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for key, value in count.items():
        if value > 1:
            dups.append(key)
    return dups

print(duplicates('abcaabd'))

    

