import unittest

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

    def degree(self, vertex):
        degree = len(self.adjacency_list[vertex])
        return degree

    
    

    
class Tests(unittest.TestCase):
    def test_case_1(self):
        nodes = ["A","B","C","D","E"]
        graph = Graph(nodes, True)
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'D')
        graph.add_edge('E', 'D')
        graph.add_edge('E', 'A')
        self.assertEqual(graph.contains('A','E'), False)
        self.assertEqual(graph.contains('A','B'), True)

    def test_case_2(self):
        nodes = ["A","B","C","D","E"]
        graph = Graph(nodes, True)
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'D')
        graph.add_edge('E', 'D')
        graph.add_edge('E', 'A')
        self.assertEqual(graph.degree('E'),2)
    
    def test_case_3(self):
        nodes = ["A","B","C","D","E"]
        graph = Graph(nodes, True)
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'D')
        graph.add_edge('E', 'D')
        graph.add_edge('E', 'A')
        self.assertEqual(graph.degree('A'),1)

    def test_case_4(self):
        nodes = ["A","B","C","D","E"]
        graph = Graph(nodes, False)
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'D')
        graph.add_edge('E', 'D')
        graph.add_edge('E', 'A')
        self.assertEqual(graph.degree('A'),2)


if __name__ == '__main__':
    unittest.main()
