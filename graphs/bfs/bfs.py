def bfs(G, start):
    n = len(G)
    vis = [False for v in range(n)]
    vis[start] = True

    Q = queue()
    Q.append(start)

    while Q:
        node = Q.popleft()
        for nbr in G[node]:
            if not vis[nbr]:
                vis[nbr] = True
                Q.append(nbr)
    return vis