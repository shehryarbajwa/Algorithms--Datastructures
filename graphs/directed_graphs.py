def create_adj_list(edges, nodes):
    graph = [[] for _ in range(nodes)]

    for u, v in edges:
        graph[u].append(v)

    return graph

print(create_adj_list([(0,1),(1,2)],3))


def create_adj_matrix(edges, nodes):
    graph = [[None for _ in range(nodes)] for _ in range(nodes)]

    for u, v in edges:
        graph[u][v] = True

    return graph