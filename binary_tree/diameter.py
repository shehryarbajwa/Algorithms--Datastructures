def diameter(root):
    longest = 0

    def visit(node):
        #base case no node
        if not node:
            return 0
        #DFS on leaf nodes
        left_height = visit(node.left)
        right_height = visit(node.right)

        nonlocal longest
        longest = max(longest, left_height + right_height)

        return 1 + max(left_height, right_height)

    visit(root)
    return longest