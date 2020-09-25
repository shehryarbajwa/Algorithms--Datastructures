def detect_cycle(graph, start):
    visited = set()

    def recursive_helper(current_vertex, parent):
        visited.add(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if recursive_helper(neighbor, current_vertex):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(len(graph)):
        if i not in visited:
            if recursive_helper(i, -1):
                return True
    return False
    

    
