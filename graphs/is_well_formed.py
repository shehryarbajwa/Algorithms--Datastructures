def is_well_formed(graph):

    n = len(graph)
    neighbour_set = [set(graph[node]) for node in range(n)]

    # Check 1
    # We traverse the vertices and edges
    # Check all entries in the list are between 0 - n - 1
    for node in range(n):
        for neighbor in graph[node]:
            if neighbor < 0 or neighbor >= n:
                return False

    # Check 2
    # We traverse just the vertices
    # Graph has no self loops
    for node in range(n):
        if node in neighbour_set[node]:
            return False

    # Check 3
    # We traverse just the vertices
    # No repeated edges - If there were, they would be in neighbour set
    for node in range(n):
        if len(neighbour_set[node]) != len(graph[node]):
            return False

    # Check 4
    # O(n + m) we traverse vertices and edges
    # Every edge appears in the list of both end points
    # We first check the nodes
    # Then we check the neighbour of the current node we are on
    # Then we check whether this node exists in the neighbour node's neighbours
    for node in range(n):
        for neighbor in graph[node]:
            if node not in neighbour_set[neighbor]:
                return False


    return True





    