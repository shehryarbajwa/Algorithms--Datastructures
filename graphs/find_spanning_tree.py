def spanning_tree(G, s):
    n = len(G)
    vis = n * [False]
    vis[0] = True
    T = [[] for v in range(n)]

    def visit(v):
        for nbr in G[v]:
            if not vis[nbr]:
                vis[nbr] = True
                T[v].append(nbr)
                T[nbr].append(v)
                visit(nbr)
    visit(s)
    return T

print(spanning_tree([[1,2],[0,2],[0,1]], 0))