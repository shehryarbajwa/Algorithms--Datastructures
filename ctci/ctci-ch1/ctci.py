import unittest

class Tree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def merge_binary(self, s, t):

        root = Tree()

        if s and t:
            root.value = s.value + t.value
            root.left = self.merge_binary(s.left, t.left)
            root.right = self.merge_binary(s.right, t.right)

        elif s:
            root.value = s.value
            root.left = s.left
            root.right = s.right

        elif t:
            root.value = t.value
            root.left = t.left
            root.right = t.right
        else:
            root.value = None

        return root



class Tests(unittest.TestCase):
    def test_case_1(self):
        t1 = Tree(3)
        t1.left = Tree(2)
        t1.right = Tree(4)
        t1.left.left = Tree(1)
        t1.left.right = Tree(3)

        t2 = Tree(5)
        t2.left = Tree(3)
        t2.right = Tree(7)
        t2.left.left = Tree(2)

        t3 = Tree(8)
        t3.left = Tree(5)
        t3.right = Tree(11)
        t3.left.left = Tree(3)
        t3.left.right = Tree(3)

        t4 = Tree()

        self.assertEqual(t4.merge_binary(t1, t2).value, t3.value)


if __name__ == "__main__":
    unittest.main()