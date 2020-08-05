def rotate(matrix):
        row_lower_bound = 0
        col_lower_bound = 0
        row_upper_bound = len(matrix) - 1
        col_upper_bound = len(matrix[0]) - 1
        
        while row_lower_bound < row_upper_bound and col_lower_bound < col_upper_bound:
            
            #traverse matrix to the right
            temp = matrix[row_lower_bound][row_lower_bound]
            matrix[row_lower_bound][col_upper_bound] = temp

        return matrix
            

print(rotate(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
))