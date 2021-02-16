def walls_and_gates(rooms):
    if not rooms:
        return

    visited = set()

    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == 0:
                bfs(row, col, rooms, visited)

    return rooms


def bfs(row, col, rooms, visited):

    queue = deque()

    #Add neighbours and value of 1 to all neighbours
    queue.append(row + 1, col, 1)
    queue.append(row - 1, col, 1)
    queue.append(row, col + 1, 1)
    queue.append(row, col - 1, 1)

    while queue:
        c_row, c_col, value = queue.pop()

        if c_row < 0 or c_row > len(rooms) - 1 or c_col < 0 or c_col > len(rooms[0]) - 1 or rooms[c_row][c_col] == 0 or rooms[c_row][c_col] == -1 or (c_row, c_col) in visited:
            return
        if visited[c_row][c_col]:
            continue
        visited.add((c_row, c_col))
        rooms[c_row][c_col] = min(rooms[c_row][c_col], value)

        queue.append(c_row + 1, c_col, value + 1)
        queue.append(c_row - 1, c_col, value + 1)
        queue.append(c_row, c_col + 1, value + 1)
        queue.append(c_row, c_col - 1, value + 1)



