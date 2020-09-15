def dfs(graph, start):
    visited = set()

    def recurse(current_vertex):
        visited.add(current_vertex)
        for v in graph[current_vertex]:
            if v not in visited:
                recurse(v)
    recurse(start)
    return visited

print(dfs([[1,2], [0,2,4], [0,1,3], [2], [1]],0))