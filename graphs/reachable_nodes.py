def reachable_nodes(G, source):
    n = len(G)
    visited = [False for _ in range(n)]
    visited[source] = True

    def visit(node):

        for neighbor in G[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                visit(neighbor)

    visit(source)
    return [v for v in range(n) if visited[v]]


