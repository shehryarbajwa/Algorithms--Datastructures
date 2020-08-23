def diagonal_traverse(matrix):
    diagonal = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + j not in diagonal:
                diagonal[i + j] = [matrix[i][j]]
            else:
                diagonal[i + j].append(matrix[i][j])

    res = []
    #Avg time O(N)

    for key, value in diagonal.items():
        if key % 2 == 0:
            right = len(value) - 1
            #Worst case O(N)
            #Average case log(n)
            
            while right >= 0:
                res.append(value[right])
                right -= 1
        else:
            for x in value:
                res.append(x)
    return value



        

