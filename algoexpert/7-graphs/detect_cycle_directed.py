
def is_cyclic_directed_graph(graph):
    # set is used to mark visited vertices
    visited = set()
    # set is used to keep track the ancestor vertices in recursive stack.
    ancestors = set()

    def is_cyclic_recur(current_vertex):
        # mark it visited
        visited.add(current_vertex)
        # add it to ancestor vertices
        ancestors.add(current_vertex)

        # Recur for all the vertices adjacent to current_vertex
        for v in graph[current_vertex]:
            # If the vertex is not visited then recurse on it
            if v not in visited:
                if is_cyclic_recur(v):
                    return True
            elif v in ancestors:
                # found a back edge, so there is a cycle
                return True

        # remove from the ancestor vertices
        ancestors.remove(current_vertex)
        return False

    # call recur for all vertices
    for u in range(len(graph)):
        # Don't recur for u if it is already visited
        if u not in visited:
            if is_cyclic_recur(u):
                return True
    return False

print(is_cyclic_directed_graph([[], [2,3], [4], [], []]))