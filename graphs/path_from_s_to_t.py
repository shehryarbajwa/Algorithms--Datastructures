def path_from_source_to_destination(G, source, destination):
    
    n = len(G)
    pred = [-1 for _ in range(n)]
    pred[source] = None

    def visit(node):

        for neighbor in G[node]:
            if pred[neighbor] == -1:
                pred[neighbor] = node
                visit(neighbor)

    
    visit(source)
    path = [destination]
    #While destination is not source
    while path[-1] != source:
        current_node = pred[path[-1]]
        if current_node == -1:
            return False
        path.append(current_node)
    
    path.reverse()
    return path


