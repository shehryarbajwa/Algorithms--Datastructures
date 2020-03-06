
#Adjacency List
#Time Complexity O(V+ E)
#Space Complexity O(V)

graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D','E'],
         'C': ['F', 'G' , 'A'],
         'D': ['B', 'E'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
 
print(bfs_connected_component(graph,'A'))


