def is_well_formed(graph):
    
    #1 - all entries in the adjacency list are between 0 - n - 1
    #2 - it has no self Loops
    #3 - no node has repeated neighbors
    #4 - every edge appears in the list of both end-points

    n = len(graph)

    # Check 1

    for node in range(n):
        for neighbor in graph[node]:
            if neighbor < 0 or neighbor >= n:
                return False


    