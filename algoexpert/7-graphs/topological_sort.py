from collections import deque

def topological_sort(graph):
    visited = set()
    queue = deque()

    def helper(current_vertex):
        visited.add(current_vertex)

        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                helper(neighbour)
        
        queue.appendleft(current_vertex)
    for u in range(len(graph)):
        if u not in visited:
            helper(u)
    return list(queue)

print(topological_sort([[1,2], [2], [3], [], [1]]))