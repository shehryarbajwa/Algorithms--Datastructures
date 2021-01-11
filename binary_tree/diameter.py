def diameter(root):
    longest = 0

    def visit(node):
        if not node:
            return 0

        l_length = visit(node.left)
        r_length = visit(node.right)

        highest = max(l_length)
        lowest = max(r_length)

        nonlocal longest
        longest = max(longest, highest + lowest)

        


    visit(root)
    return longest