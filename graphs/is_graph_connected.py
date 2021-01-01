import unittest

def is_connected(graph):
    n = len(graph)
    visited = [False for _ in range(n)]

    def visit(node):
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                visit(neighbor)

    visit(0)
    return all(visited)


class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_connected([[1,2],[0,2],[0,1]]), True)

    def test_case_2(self):
        self.assertEqual(is_connected([[1],[2],[3],[],[5]]), False)


if __name__ == "__main__":
    unittest.main()
