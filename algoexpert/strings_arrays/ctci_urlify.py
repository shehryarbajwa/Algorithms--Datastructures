
#Time Complexity O(N)
# Space Complexity O(1) since we take the input string, convert it into list, use all its extra whitespace characters
# Then add the %20 to them and finally return the string with the url.
# Since done in place, space is constant. We are not using extra memory for storing the string

def urlify(string,length):
    space_count = 0
    for i in range(len(string)):
        if string[i] == ' ':
            space_count += 1

    index = (length + space_count * 2)

    string = list(string)

    for f in range(len(string) - 1, index - 1): 
        string.append('0') 
    

    for i in range(length - 1, 0, -1):
        if string[i] == ' ':
            string[index - 1] = '0'
            string[index - 2] = '2'
            string[index - 3] = '%'
            index = index - 3
        else:
            string[index - 1] = string[i]
            index -= 1
    
    return "".join(string)
    

print(urlify('Mr John Smith', 13))