def is2Colorable(graph):
    n = len(graph)
    color = [-1] * n


    def is2colored(node):
        for neighbor in graph[node]:
            if color[neighbor] == color[node]:
                return False

            if not color[neighbor]:
                color[neighbor] = 1 if color[node] == 0 else 1

                if not is2colored(neighbor):
                    return False
        return True

    for u in range(n):
        if not color[u]:
            color[u] = 0

            if not is2colored(u):
                return False
    return True