def max_in_degree(graph):
    
    n = len(graph)
    in_degree = [0 for node in range(n)]

    for node in range(n):
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    final = float('-inf')
    for node in range(n):
        final = max(final, in_degree[node])

    return final
