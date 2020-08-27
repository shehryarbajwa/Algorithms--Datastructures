#In-place
def transpose(array):
    end_row = len(array)
    end_col = len(array[0])

    for row in range(end_row):
        for col in range(row + 1, end_col):
            array[row][col], array[col][row] = array[col][row], array[row][col]

    return array
#Extra space
def transpose_matrix(array):
    rows = len(array)
    cols = len(array[0])
    new_matrix = [[0 for x in range(rows)] for y in range(cols)]

    for row in range(len(array)):
        for col in range(len(array)):
            new_matrix[row][col] = array[col][row]

    return new_matrix



print(transpose([[1,2,3],[4,5,6]]))
print(transpose_matrix([[1,2,3],[4,5,6]]))