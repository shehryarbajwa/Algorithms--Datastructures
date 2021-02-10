def num_islands(graph):
    num_islands = 0

    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == '1':
                dfs(row, col, graph)
                num_islands += 1
    return num_islands

def dfs(row, col, graph):

    if row < 0 or row >= len(graph) or col < 0 or col >= len(graph) or graph[row][col] != '1':
        return

    graph[row][col] = 'None'

    dfs(row + 1, col, graph)
    dfs(row - 1, col, graph)
    dfs(row, col + 1, graph)
    dfs(row, col - 1, graph)


