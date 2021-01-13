def detect_cycle(graph):
    n = len(graph)
    visited = set()

    def visit(node, parent):
        for neighbor in graph[node]:
            if visited[neighbor] and neighbor != parent:
                return True

            if not visited[neighbor]:
                visited[neighbor] = True
                if visit(neighbor, node):
                    return True
        return False

    for i in range(n):
        if i not in visited:
            visited[i] = True

            if visit(i, -1):
                return True
    return False

