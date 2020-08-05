

# test 'abc   ' - len(6)

def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    space_count = 0
    for i in range(len(string)):
        if string[i] == ' ':
            space_count += 1

    index = length + (space_count * 2)

    string = list(string)

    for f in range(len(string) - 1, index - 1): 
        string.append('0') 
    
    for i in reversed(range(length)):
        
        if string[i] == ' ':
            string[index - 1] = '0'
            string[index - 2] = '2'
            string[index - 3] = '%'
            index = index - 3
        else:
            #string 16 = h - index 16
            #string 15 = t - index 15
            #string 14 = i - index 14
            #string 13 = m - index 13
            #string 12 = s - index 12

            
            string[index - 1] = string[i]
            index -= 1
    
    return "".join(string)

print(urlify('Mr John Smith', 13))
