class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def ten_conseuctive(root):
    prev = None
    streak = 0
    res = False
    def visit(node):
        if not node:
            return
        visit(node.left)
        nonlocal prev, streak, res
        
        if prev != None and node.value == prev + 1:
            streak += 1
        else:
            streak = 1

        if streak == 10:
            res = True
        prev = node.value

        visit(node.right)
    visit(root)
    return res


Tree = Node(10)
Tree.left = Node(7)
Tree.right = Node(14)
Tree.left.left = Node(5)
Tree.left.left.left = Node(1)
Tree.left.left.right = Node(6)
Tree.left.right = Node(8)
Tree.left.right.right = Node(9)
Tree.right.left = Node(12)
Tree.right.left.left = Node(11)
Tree.right.left.right = Node(13)
Tree.right.right = Node(18)

print(ten_conseuctive(Tree))
# print(validate_sequence(in_order_traversal(Tree, [])))