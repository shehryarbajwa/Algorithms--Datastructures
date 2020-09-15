def dfs(graph, start):
    visited = []

    def recurse(current_vertex):
        visited.append(current_vertex)
        for v in graph[current_vertex]:
            if v not in visited:
                recurse(v)
    recurse(start)
    return visited

def dfs_iterative(graph, start):
    visited = []
    stack = []
    stack.append(start)

    while stack:
        current_vertex = stack.pop()
        if current_vertex not in visited:
            visited.append(current_vertex)

        for v in graph[current_vertex]:
            if v not in visited:
                stack.append(v)
    return visited







print(dfs([[1,2], [0,2,4], [0,1,3], [2], [1]],0))
print(dfs_iterative([[1,2], [0,2,4], [0,1,3], [2], [1]],0))