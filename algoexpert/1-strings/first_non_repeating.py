

def first_non_repeating(string):
    if not string:
        return False
    dups = {}
    index = 0
    for i in range(len(string)):
        if string[i] in dups:
            dups[string[i]] += 1
        else:
            dups[string[i]] = 1
    
    for i in range(len(string)):
        if dups[string[i]] == 1:
            index = i
            break
        else:
            continue
    return string[index]

print(first_non_repeating('hello'))
