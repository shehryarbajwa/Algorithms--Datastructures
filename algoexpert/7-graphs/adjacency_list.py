#Undirected graph


class Graph:
    def __init__(self, nodes, is_directed=False):
        self.is_directed = is_directed
        self.nodes = nodes
        self.adjacency_list = {}

    def populate_adjacency_list(self):
        for node in self.nodes:
            self.adjacency_list[node] = []

    def add_edge(self, node, vertex):
        self.adjacency_list[node].append(vertex)
        if self.is_directed == False:
            self.adjacency_list[vertex].append(node)

    def degree(self, node):
        return len(self.adjacency_list[node])

    def print_adjacency_list(self):
        for node in self.nodes:
            print(node, ' ->', self.adjacency_list[node])

nodes = ['A', 'B', 'C', 'D', 'E']
g = Graph(nodes)
g.populate_adjacency_list()

g.add_edge('A', 'B')
g.add_edge('B', 'D')
g.add_edge('D', 'E')
g.add_edge('E', 'C')
g.add_edge('C', 'A')
g.add_edge('C', 'D')

g.print_adjacency_list()
    