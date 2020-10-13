#Time Complexity O(N + M)
#If we search the entire thing it will be O(N * M)
#Space Complexity O(1)
def search_sorted_matrix(matrix, target):
    row, col = 0, len(matrix) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return [row, col]
        elif matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -= 1
    return [-1,-1]



