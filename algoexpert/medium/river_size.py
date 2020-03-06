# You are given a two-dimensional array(matrix) of unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river.
# A river consists of any number of 1s that are either horizontally or vertically adjacent.
# Write a function that returns an array of the size of all rivers represented in the input matrix.


# Sample Matrix: 

# [
    # [1,0,0,1,0],
    # [1,0,1,0,0],
    # [0,0,1,0,1],
    # [1,0,1,0,1],
    # [1,0,1,1,0]
# ]

def riverSizes(matrix):
    sizes = []

    #For row in matrix leads to 5 rows.
    #For value in row leads to values in row.
    #We create a dynamic array of False for each value in row.
    visited = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j] == True:
                continue
            else:
                traverseNode(i, j, matrix, visited,sizes)
    return sizes

def traverseNode(i, j , matrix, visited, sizes ):
    currentRiverSize = 0
    nodeToExplore = [[i,j]]

    while len(nodeToExplore):
        currentNode = nodeToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]

        if visited[i][j] == True:
            continue
        visited[i][j] == True

        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        





