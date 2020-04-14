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
            print(node, ' -> ', self.adjacency_list[node])

    def degree(self, vertex):
        degree = len(self.adjacency_list[vertex])
        return degree

    def BFS(self, root):
        visited = []
        queue = [root]

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.append(current)
                neighbours = self.adjacency_list[current]
                for neighbour in neighbours:
                    queue.append(neighbour)

        return visited

    def DFS(self, root, visited):
        visited.append(root)

        for v in self.adjacency_list[root]:
            if v not in visited:
                self.DFS(v, visited)

        return visited

    def is_cyclic_util(self, vertex, visited, parentNode):

        visited[vertex] = True

        for vertice in self.adjacency_list[vertex]:
            if visited[vertice] == False:
                if (self.is_cyclic_util(vertice, visited, vertex)):
                    return True
            elif parentNode != vertice:
                return True
        return False


    def is_cyclic(self):

        visited = [None] * len(self.adjacency_list)

        for i in range(len(self.adjacency_list)):
            if visited[i] == False:
                if (self.is_cyclic_util(i, visited, -1)) == True:
                    return True
        return False


nodes = ["A","B","C","D","E"]
graph = Graph(nodes, True)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'E')
graph.add_edge('B', 'E')
graph.add_edge('B', 'A')
graph.add_edge('C', 'A')
graph.add_edge('C', 'D')
graph.add_edge('D', 'C')
graph.add_edge('E', 'A')
graph.add_edge('E', 'B')


graph.print_adjacency_list()
print(graph.is_cyclic())




    
# class Tests(unittest.TestCase):
#     def test_case_1(self):
#         nodes = ["A","B","C","D","E"]
#         graph = Graph(nodes, True)
#         graph.add_edge('A', 'B')
#         graph.add_edge('B', 'C')
#         graph.add_edge('C', 'D')
#         graph.add_edge('E', 'D')
#         graph.add_edge('E', 'A')
#         self.assertEqual(graph.BFS('A'),['A', 'B', 'C', 'D'])
#         self.assertEqual(graph.contains('A','E'), False)
#         self.assertEqual(graph.contains('A','B'), True)

#     def test_case_2(self):
#         nodes = ["A","B","C","D","E"]
#         graph = Graph(nodes, True)
#         graph.add_edge('A', 'B')
#         graph.add_edge('B', 'C')
#         graph.add_edge('C', 'D')
#         graph.add_edge('E', 'D')
#         graph.add_edge('E', 'A')
#         self.assertEqual(graph.degree('E'),2)
    
#     def test_case_3(self):
#         nodes = ["A","B","C","D","E"]
#         graph = Graph(nodes, True)
#         graph.add_edge('A', 'B')
#         graph.add_edge('B', 'C')
#         graph.add_edge('C', 'D')
#         graph.add_edge('E', 'D')
#         graph.add_edge('E', 'A')
#         self.assertEqual(graph.degree('A'),1)

#     def test_case_4(self):
#         nodes = ["A","B","C","D","E"]
#         graph = Graph(nodes, False)
#         graph.add_edge('A', 'B')
#         graph.add_edge('B', 'C')
#         graph.add_edge('C', 'D')
#         graph.add_edge('E', 'D')
#         graph.add_edge('E', 'A')
#         self.assertEqual(graph.degree('A'),2)


# if __name__ == '__main__':
#     unittest.main()
