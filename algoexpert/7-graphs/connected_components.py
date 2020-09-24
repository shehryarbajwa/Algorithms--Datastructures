from collections import defaultdict

def connected_components(n, edges):
    adj_list = defaultdict(list)
    visited = {}
    count = 0
    
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    def dfs(edge):
        visited[edge] = True
        for neighbor in adj_list[edge]:
            if neighbor not in visited:
                dfs(neighbor)

    for i in range(len(edges)):
        if i not in visited:
            dfs(edges[i])
            count += 1
    return count

    
