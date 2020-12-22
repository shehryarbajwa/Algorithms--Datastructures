def create_adj_list(edges, nodes):
    graph = [[] for _ in range(nodes)]

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, v))

    return graph

def create_adj_matrix(edges, nodes):
    graph = [[None for _ in range(nodes)] for _ in range(nodes)]

    for u, v, w in edges:
        graph[u][v] = w
        graph[v][u] = w

    return graph
