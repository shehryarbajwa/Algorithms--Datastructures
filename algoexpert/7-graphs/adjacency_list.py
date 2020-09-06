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



    