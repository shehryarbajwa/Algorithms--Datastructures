def as_far_from_land(matrix):
    max_distance = float('-inf')
    directions = ((1,0),(0,1),(-1,0),(0,-1))
    queue = collections.deque()
    visited = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                queue.append((row, col, 0))


    if len(queue) == 0:
        return -1

    #Checks
    # 1-In BFS, check if the nbr is 0 or 1
    # 2-
    while queue:
        r, c, distance = queue.popleft()
        max_distance = max(max_distance, distance)

        for direction in directions:
            new_row = r + direction[0]
            new_col = c + direction[1]

        if new_row >= 0 and new_row <= len(matrix) - 1 and new_col >= 0 and new_col <= len(matrix[0]) - 1 and (new_row, new_col) not in visited and matrix[new_row][new_col] == 0:
            queue.append((new_row, new_col, distance + 1))
            visited.add((new_row, new_col))
    return distance



    


    



    
