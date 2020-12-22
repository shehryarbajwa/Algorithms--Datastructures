def create_adj_list(n, edge_list):

    G = [[] for v in range(n + 1)]

    for u, v in edge_list:
        G[u].append(v)
        G[v].append(u)
        
    return G[1:]

print(create_adj_list(3, [[2,3],[1,3],[1,2]]))