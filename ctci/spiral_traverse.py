# Example [[1,2,3]
#          [4,5,6],
#          [7,8,9]]
#           ]]

def spiral_traverse(matrix):

    row_lower_bound = 0
    row_upper_bound = len(matrix) - 1
    col_lower_bound = 0
    col_upper_bound = len(matrix[0]) - 1
    output = []

    while row_lower_bound < row_upper_bound and col_lower_bound < col_upper_bound:

        #Move right
        for i in range(col_lower_bound, col_upper_bound + 1):
            output.append(matrix[row_lower_bound][i])
        
        #Move vertically down
        for i in range(row_lower_bound + 1, row_upper_bound + 1):
            output.append(matrix[i][col_upper_bound])

        #Move left
        for i in reversed(range(col_lower_bound, col_upper_bound)):
            output.append(matrix[row_upper_bound][i])

        #Move up
        for i in reversed(range(row_lower_bound + 1, row_upper_bound)):
            output.append(matrix[i][col_lower_bound])



        #Finishing one full cycle
        row_lower_bound += 1
        row_upper_bound -= 1
        col_lower_bound += 1
        col_upper_bound -= 1
        
    return output
            
print(spiral_traverse([[1, 2, 3], [4,5,6], [7,8,9]]))