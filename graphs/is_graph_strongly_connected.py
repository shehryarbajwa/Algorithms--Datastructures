def is_strongly_connected(G, source):
    n = len(G)
    visited = [False for _ in range(n)]


    def visit(node):
        for neighbor in G[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                visit(neighbor)

    visit(source)
    if not all(visited):
        return False

    