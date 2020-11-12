class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def ten_conseuctive(root):
    output = 0
    res = False
    def visit(node, node_path, parent):

        nonlocal output, res
        output = max(output, node_path)

        if not node:
            return
        
        if not parent or (parent.value - node.value) == -1:
            node_path += 1
        else:
            node_path = 1
        
        if node_path == 10:
            res = True
        
        visit(node.left, node_path, node)
        visit(node.right, node_path, node)
            
        
    visit(root, 0, None)
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