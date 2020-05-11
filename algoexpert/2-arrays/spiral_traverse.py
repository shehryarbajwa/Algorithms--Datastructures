
#Iterative Solution 
#O(N) Time Complexity
#Space Complexity O(N)
def spiral_traverse(array):

    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1

    result = []

    while start_row <= end_row and start_col <= end_col:

        #Move forward
        for col in range(start_col, end_col + 1):
            result.append(array[start_col][col])

        #Move downwards excluding the start column
        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])

        #Move backwards excluding the end column
        for col in reversed(range(start_col, end_col)):
            result.append(array[end_row][col])

        #Move upwards excluding the end row
        for row in reversed(range(start_row + 1, end_row)):
            result.append(array[row][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return result

#Recursive Solution
#Time Complexity O(N)
#Space Complexity O(N)

def spiralTraverse(array):
    # Write your code here
	
	result = []
	spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
	return result

def spiralFill(array, startRow, endRow, startCol, endCol, result):
	
	if startRow > endRow or startCol > endCol:
		return
	
	for col in range(startCol, endCol + 1):
		result.append(array[startRow][col])
	
	for row in range(startRow + 1, endRow + 1):
		if startRow == endRow:
			break
		result.append(array[row][endCol])
		
	for col in reversed(range(startCol, endCol)):
		if startRow == endRow:
			break
		result.append(array[endRow][col])
		
	for row in reversed(range(startRow + 1, endRow)):
		if startCol == endCol:
			break
		result.append(array[row][startCol])
		
	spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)
    


        

        