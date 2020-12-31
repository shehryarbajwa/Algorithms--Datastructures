def can_s_reach_t(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    visited[s] = True

    def visit(node):
        
        for neighbor in G[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                visit(neighbor)

    return True if visited[t] == True else False
