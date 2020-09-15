from collections import deque

# graph: List[List[int]]
# s: start vertex
def bfs(graph, s):
    visited = set()
    queue = []
    visited.add(s)
    queue.append(s)

    while queue:
        current_vertex = queue.pop()
        for v in graph[current_vertex]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return visited


print(bfs([[1,2], [0,2,4], [0,1,3], [2], [1]],0))