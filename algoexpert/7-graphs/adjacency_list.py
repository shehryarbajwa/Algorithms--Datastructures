#Build a graph via Adjacency List
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

    def depth_first_search(self, visited, node):
        if node in visited:
            return
        else:
            visited.append(node)
            for neighbor in self.adjacency_list[node]:
                self.depth_first_search(visited, neighbor)
        return visited
        

    def breath_first_search(self, array, node):
        array = [node]
        queue = [node]

        while queue:
            current_node = queue.pop(0)
            for neighbour in self.adjacency_list[current_node]:
                if neighbour not in array:
                    array.append(neighbour)
                    queue.append(neighbour)
        return array

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
print(g.depth_first_search([], nodes[0]))
# print(g.breath_first_search([], nodes[0]))

print('\n')
# nodes = ['A', 'B', 'C', 'D', 'E']
# g2 = Graph(nodes, True)
# g2.populate_adjacency_list()

# g2.add_edge('A','B')
# g2.add_edge('A','C')
# g2.add_edge('B','D')
# g2.add_edge('C','D')
# g2.add_edge('C','E')
# g2.add_edge('D','E')

# g2.print_adjacency_list()
    