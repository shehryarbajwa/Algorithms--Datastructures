def river_sizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverse(i, j,matrix, sizes, visited)
    return sizes

def traverse(i, j, matrix, sizes,visited):
    current_river_size = 0
    nodes_to_explore = [[i,j]]

    while len(nodes_to_explore) > 0:
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_river_size += 1
        getUnivisitedNeighours = getUnivisitedNeighours(i,j,matrix, visited)
        for neighbor in getUnivisitedNeighours:
            nodes_to_explore.append(neighbor)
    if current_river_size > 0:
        sizes.append(current_river_size)

def getUnivisitedNeighours(i,j,matrix, visited):
    univisitedNeighours = []
    if i > 0 and not visited[i - 1][j]:
        univisitedNeighours.append([i - 1][j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        univisitedNeighours.append([i + 1][j])
    if j > 0 and not visited[i][j - 1]:
        univisitedNeighours.append([i][j - 1])
    if j < len(matrix)[i] - 1 and not visited[i][j + 1]:
        univisitedNeighours.append([i][j + 1])
    return unvisitedNeighours





            