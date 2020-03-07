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

#time Complexity is O(Width * Height)
#Space Complexity is O(Width * height)

import unittest

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

        univisitedNeighours = getUnivisitedNeighours(i, j, matrix, visited)

        for neighbour in univisitedNeighours:
            nodeToExplore.append(neighbour)

    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnivisitedNeighours(i, j, matrix, visited):
    univisitedNeighours = []

    #First rule. If we are not in the top row
    #E.g we are in the second row
    # i = 1
    #We need to add the element at i =0, so we move up
    #If we are not in the first row, and we have not visited the element on top of existing element then we add it
    #Move vertically up
    if i > 0 and not visited[i-1][j]:
        univisitedNeighours.append([i-1, j])
    #Second rule. If we are not in the bottom row
    #E.g we are in the second last row
    #i = 3, we need to add the element at i = 4
    #Move vertically down
    #Then we move down vertically and add the node that is on the bottom row
    if i < len(matrix) - 1 and not visited [i + 1][j]:
        univisitedNeighours.append([i + 1, j])
    
    #Move horizontally to the left

    if j > 0 and not visited [i][j - 1]:
        univisitedNeighours.append([i, j - 1])

    #Move horizontally to the right
    #Matrix is 0 because we are moving horizontally so matrix[0] refers to the row width
    #len(matrix) refers to the column width
    if j < len(matrix[0]) - 1 and not visited [i][j + 1]:
        univisitedNeighours.append([i, j + 1])

    return univisitedNeighours


class Test(unittest.TestCase):
    def test_case_1(self):
        matrix = [[]]
        expected = [[]]
        self.assertEqual(riverSizes(matrix), expected)

    def test_case_2(self):
        testInput = [[1]]
        expected = [1]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_3(self):
        testInput = [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]]
        expected = [1, 2, 3]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_4(self):
        testInput = [[1, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 0], [1, 0, 1, 0]]
        expected = [1, 1, 2, 3]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

if __name__ == "__main__":
    unittest.main()

    