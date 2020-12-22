def create_adj_list(edges, amount_of_vertices):

    graph = [[] for _ in range(amount_of_vertices)]

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def create_adj_matrix(edges, amount_of_vertices):

    graph = [[None for _ in range(amount_of_vertices)] for _ in range(amount_of_vertices)]

    for u,v in edges:
        graph[u][v] = True
        graph[v][u] = True
    return graph

print(create_adj_list([(0,1),(1,2),(0,2)],3))
print(create_adj_matrix([(0,1),(1,2),(0,2)],3))