def total_connected_components(graph):
    n = len(graph)
    visited = [False for _ in range(n)]

    def visit(node):
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                visit(neighbor)

    total_connected_components = 0

    for u in range(n):
        if not visited[u]:
            total_connected_components += 1
            visited[u] = True
            visit(u)
    
    return total_connected_components

