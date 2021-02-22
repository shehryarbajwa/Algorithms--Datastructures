def update_matrix(matrix):
    if not matrix:
        return


    directions = ((1,0),(0,1),(-1,0),(0,-1))
    new_distance = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                
                queue = collections.deque()
                queue.append(row, col, 0)

                while queue:
                    r, c, distance = queue.popleft()
                    new_distance = distance

                    if matrix[r][c] == 0:
                        break

                    for dirr in directions:
                        new_row = r + dirr[0]
                        new_col = c + dirr[1]

                        if new_row >= 0 and new_row <= len(matrix[row] - 1) and new_col >= 0 and new_col <= len(matrix[0]) - 1:
                            queue.append((new_row, new_col, distance + 1))

                matrix[row][col] = new_distance
    return matrix