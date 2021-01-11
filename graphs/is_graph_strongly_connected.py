def is_strongly_connected(G, source):
    n = len(G)
    visited = [False for _ in range(n)]


    def visit(G, node):
        for neighbor in G[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                visit(G, neighbor)

    visit(G, source)
    if not all(visited):
        return False

    G_reverse = [[] for _ in range(n)]
    visited = [False for _ in range(n)]

    for v in range(n):
        for neighbor in G[v]:
            G_reverse[neighbor].append(v)

    visited[0] = True
    visit(G_reverse, source)
    return all(visited)


    