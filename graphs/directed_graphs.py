def create_adj_list(edges, nodes):
    graph = [[] for _ in range(nodes)]

    for u, v in edges:
        graph[u].append(v)

    return graph

graph = create_adj_list([(0,2),(2,6), (0,6)], 3)

def num_edges(graph):
    return sum(len(edge) for edge in graph)


def create_adj_matrix(edges, nodes):
    graph = [[None for _ in range(nodes)] for _ in range(nodes)]

    for u, v in edges:
        graph[u][v] = True

    return graph

print(num_edges(graph))
