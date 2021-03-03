def walls_and_gates(rooms):

    if not rooms:
        return

    directions = ((1,0),(0,1),(0,-1),(-1,0))

    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == 0:
                queue = collections.deque()
                queue.append((row, col))

                while queue:
                    current_row, current_col = queue.popleft()

                    for dirr in directions:
                        n_row, n_col = current_row + dirr[0], current_col + dirr[1]

                        if n_row >= 0 and n_row <= len(rooms) - 1 and n_col >= 0 and n_col <= len(rooms[0]) - 1 and rooms[n_row][n_col] > rooms[current_row][current_col]:
                            rooms[n_row][n_col] = rooms[current_row][current_col] + 1
                            queue.append((n_row, n_col))
    return rooms 


