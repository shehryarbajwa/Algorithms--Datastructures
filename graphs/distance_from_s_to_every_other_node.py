def get_distances(graph, s):
    n = len(graph)
    dists = n * [-1]
    dists[s] = 0

    def visit(node):
        for nbr in graph[node]:

            if dists[nbr] != -1:
                continue

            dists[nbr] = dists[node] + 1
            visit(nbr)
    visit(s)
    return dists