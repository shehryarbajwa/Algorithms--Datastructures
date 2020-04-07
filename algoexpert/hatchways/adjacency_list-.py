class Graph:
    def __init__(self, vertices, is_directed=False):
        self.vertices = vertices
        self.adjacency_list = {}
        self.is_directed = is_directed

        for v in vertices:
            self.adjacency_list[v] = []

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)

        if not self.is_directed:
            self.adjacency_list[destination].append(source)

    def contains(self, source, destination):

        for v in self.adjacency_list[source]:
            if v == destination:
                return True
        return False

    def remove_edge(self, source, destination):
        self.adjacency_list[source].remove(destination)

        if not self.is_directed:
            self.adjacency_list[destination].remove(source)

    def print_adjacency_list(self):
        for node in self.adjacency_list:
            print(node + ' -> ' + self.adjacency_list[node])
    
    
    

