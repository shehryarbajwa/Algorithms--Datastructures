

def o_notation(string):

    result = []

    for i in range(len(string)):
        for j in range(len(string)):
            result.append(string[i:j + 1])

    return result

print(o_notation('abcd'))