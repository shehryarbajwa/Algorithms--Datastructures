def longest_streak(root):
    longest = 0


    def visit(node, parent, current_streak):
        if not node:
            return
        nonlocal longest
        if node.value == parent.value:
            current_streak += 1
        else:
            current_streak = 1
        longest = max(longest, current_streak)
        visit(node.left, node.value, current_streak)
        visit(node.right, node.value, current_streak)
    
    visit(root, None, 0)
    return longest