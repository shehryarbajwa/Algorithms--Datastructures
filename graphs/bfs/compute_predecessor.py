def compute_predecessor(G, start):
    n = len(G)
    pred = [-1 for _ in range(n)]
    pred[start] = None

    q = deque()
    q.append(start)

    while q:
        node = q.popleft()

        for nbr in G[node]:
            if pred[nbr] == -1:
                pred[nbr] = node
                q.append(nbr)

    return pred

    
