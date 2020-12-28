def create_adj_list(adjacency_matrix):
    n = len(adjacency_matrix)
    graph = [[] for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if adjacency_matrix[row, col] == True:
                graph[row].append(col)
    return graph

    
