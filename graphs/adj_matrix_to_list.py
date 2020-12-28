def create_adj_list(adjacency_matrix):
    n = len(adjacency_matrix)
    graph = [[] for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if adjacency_matrix[row][col] == True:
                graph[row].append(col)
    return graph

def neighbours_of_vip_nodes(vip_nodes, graph):
    
    neighbours_list = [[] for _ in range(len(graph))]

    for node in vip_nodes:
        for neighbor in graph[node]:
            neighbours_list[neighbor] = True

    return [node for node in neighbours_list if neighbours_list[node]]
