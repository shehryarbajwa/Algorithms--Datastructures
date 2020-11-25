def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def num_leaves(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1
    return num_leaves(root.left) + num_leaves(root)
    

