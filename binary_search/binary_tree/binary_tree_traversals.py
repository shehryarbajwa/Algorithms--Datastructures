def in_order_traversal(root, array):
    if root is not None:
        in_order_traversal(root.left, array)
        array.append(root.value)
        in_order_traversal(root.right, array)
    return array

def post_order_traversal(root, array):
    if root is not None:
        post_order_traversal(root.left, array)
        post_order_traversal(root.right, array)
        array.append(root.value)
    return array

def pre_order_traversal(root, array):
    if root is not None:
        array.append(root.value)
        pre_order_traversal(root.left, array)
        pre_order_traversal(root.right, array)
    return array