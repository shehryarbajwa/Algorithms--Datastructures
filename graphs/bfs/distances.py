def bfs_distances(G, source):
    n = len(G)
    distances = [-1 for _ in range(n)]
    distances[source] = 0

    q = queue()
    q.append(source)

    while q:
        node = q.popleft()
        for neighbor in G[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                q.append(neighbor)
    return distances


