def distance_to_closest_nodes(G, special_nodes):
    n = len(G)
    distance = [-1 for _ in range(n)]
    Q = deque()

    for node in special_nodes:
        distance[node] = 0
        Q.append(node)

    while Q:
        current_node = Q.pop()
        for nbr in G[current_node]:
            if distance[nbr] == -1:
                Q.append(nbr)
                distance[nbr] = distance[current_node] + 1
    return distance