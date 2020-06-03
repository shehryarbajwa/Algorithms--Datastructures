def in_order_traversal(node,array):
    if node is not None:
        in_order_traversal(node.left,array)
        array.append(node.value)
        in_order_traversal(node.right,array)
    return array

def pre_order_traversal(node,array):
    if node is not None:
        array.append(node.value)
        pre_order_traversal(node.left,array)
        pre_order_traversal(node.right, array)
    return array

def post_order_traversal(node,array):
    if node is not None:
        post_order_traversal(node.left,array)
        post_order_traversal(node.right,array)
        array.append(node.value)
    return array
    
