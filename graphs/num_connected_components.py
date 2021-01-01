def total_connected_components(graph):
    n = len(graph)
    visited = n * [False]

    def visit(node):
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                visit(neighbor)

    total_cc = 0
    for node in range(n):
        if not visited[node]:
            total_cc += 1
            visited[node] = True
            visit(node)
    return total_cc
