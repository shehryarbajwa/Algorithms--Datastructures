

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

def count_spaces(string):
    b_count = 0

    for char in string:
        if char == 'b':
            if b_count == 1:
                continue
            else:
                b_count += 1
        else:
            b_count = 0
    return b_count


print(first_non_repeating('hello'))
