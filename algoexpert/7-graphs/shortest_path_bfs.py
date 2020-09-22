from collections import deque

def shortest_path(graph, source, destination):
    visited = set()
    queue = deque()
    pred = [None] * len(graph)
    visited.add(source)
    queue.appendleft(source)

    #BFS traverse on neighbors
    while queue:
        current_vertex = queue.pop()

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.appendleft(neighbor)
                pred[neighbor] = current_vertex

                if neighbor == destination:
                    break
    
    if pred[destination] == None:
        return []

    #Find path

    path = [destination]
    current_vertex = destination

    while pred[current_vertex] != None:
        current_vertex = pred[current_vertex]
        path.append(current_vertex)

    return path[::-1]
    
print(shortest_path([[1,2], [0,2,4], [0,1,3], [2], [1]], 4, 0))





