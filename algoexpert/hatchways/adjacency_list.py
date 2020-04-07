
class Graph:
    def __init__(self, Nodes, is_directed=False):
        self.nodes = Nodes
        self.adjacency_list = {}
        self.is_directed = is_directed

        for node in self.nodes:
            self.adjacency_list[node] = []

    def print_adjacency_list(self):
        for node in self.nodes:
            print(node, '->', self.adjacency_list[node])

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)
        #if undirected, map destination to source aswell
        if not self.is_directed:
            self.adjacency_list[destination].append(source)

    def degree(self, node):
        degree  = len(self.adjacency_list[node])
        return degree

    def contains(self, node, destination):

        for vertex in self.adjacency_list[node]:
            if vertex == destination:
                return True
        return False

    def remove_edge(self, source, destination):
        self.adjacency_list[source].remove(destination)

        if not self.is_directed:
            self.adjacency_list[destination].remove(source)

    def BFS(self, root):

        visited = [False for _ in range(len(self.adjacency_list))]
        queue = [root]

        while queue:
            current = queue.pop(0)
            visited.append(current)
            for child in self.adjacency_list[current]:
                queue.append(child)
        return visited
            
            



nodes = ["A","B","C","D","E"]
graph = Graph(nodes, True)
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('E', 'D')
graph.add_edge('E', 'A')
print(graph.BFS('A'))


graph.print_adjacency_list()
print(graph.degree('E'))
print(graph.contains('E', 'A'))
# nodes = ["A","B","C","D","E"]
# graph = Graph(nodes)
# graph.add_edge('A', 'B')
# graph.add_edge('B', 'C')
# graph.add_edge('C', 'D')
# graph.add_edge('D', 'E')
# graph.add_edge('E', 'A')
# graph.print_adjacency_list()



