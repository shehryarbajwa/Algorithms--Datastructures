def levenshtein_distance(str1, str2):
    #First row to have default 0, 1, 2, 3, 4 , ... depending on length of str2
    rows = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    #Columns are initialized with 
    for i in range(1, len(str2) + 1):
        rows[i][0] = rows[i - 1][0] + 1
    
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                rows[i][j] = rows[i - 1][j - 1]
            else:
                rows[i][j] = 1 + min(rows[i - 1][j], rows[i][j - 1], rows[i - 1][j - 1])
    return rows[-1][-1]

    

print(levenshtein_distance('abc', 'yabc'))