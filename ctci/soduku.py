
#Check duplication of digits
#How to do that?

def valid_soduku(matrix):
    unique = set()
    start_row = 0
    start_col = 0
    end_row = len(matrix)
    end_col = len(matrix[0])

    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            if matrix[row][col] != '.':
                current_num = (matrix[row][col])

                if (row, current_num) in unique or (current_num, col) in unique or (row // 3, col // 3, current_num) in unique:
                    return False

                unique.add((row // 3, col // 3, current_num))
                unique.add((row, current_num))
                unique.add((current_num, col))
    return True

print(valid_soduku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]))