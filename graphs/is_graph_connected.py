def is_connected(graph):
    n = len(graph)
    visited = [False for _ in range(n)]

    def visit(node):
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                visit(neighbor)

    visit(0)
    return all(visited)