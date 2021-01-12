def detect_cycle(graph):
    n = len(graph)
    visited = [False for _ in range(n)]

    def visit(node, parent):
        for neighbor in graph[node]:
            if visited[neighbor] and neighbor != parent:
                return True

            if not visited[neighbor]:
                visited[neighbor] = True
                visit(neighbor, node)

    for i in range(n):
        if not visited[i]:
            visited[i] = True

            if visit(i, -1):
                return True
    return False

