# Example

# [1,2,3],
# [4,5,6],
# [7,8,9]

# [1,4,7]
# [2,5,8]
# [3,6,9]

def transpose(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = [[None] * rows for _ in xrange(cols)]
    for row, col in enumerate(matrix):
        for col, val in enumerate(row):
            new_matrix[col][row] = val
    return new_matrix

print(transpose([]))
