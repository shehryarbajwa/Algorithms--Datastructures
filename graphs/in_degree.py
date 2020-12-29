def in_degree(graph):
    n = len(graph)

    in_degree = [0 for node in range(n)]

    for node in range(n):
        for nbr in graph[node]:
            in_degree[nbr] += 1

    res = []

    for node in range(n):
        if in_degree[node] == 0:
            res.append(node)

    return res


def out_degree_zero(graph):
    n = len(graph)

    res = []
    for node in range(n):
        if len(graph[node]) == 0:
            res.append(node)

    return res