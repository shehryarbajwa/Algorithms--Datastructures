from collections import deque

# graph: List[List[int]]
# s: start vertex
def bfs(graph, s):
    # set is used to mark visited vertices
    visited = set()

    # create a queue for BFS 
    queue = []

    # Mark the start vertex as visited and enqueue it
    visited.add(s)
    queue.append(s)

    while queue:
        current_vertex = queue.pop()

        # Get all adjacent vertices of current_vertex 
        # If a adjacent has not been visited, then mark it 
        # visited and enqueue it
        for v in graph[current_vertex]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return visited

print(bfs([[1,2], [0,2,4], [0,1,3], [2], [1]],0))