def closest_value_in_bst(tree, target):
    closest = float('inf')

    def visit(node, target, closest):
        if node is None:
            return closest

        if abs(target - closest) > abs(target - node.value):
            closest = node.value

        if target < node.value:
            #recurse left
            visit(node.left, target, closest)

        elif target > node.value:
            visit(node.right, target, closest)

        else:
            closest = node.value

    visit(tree, target, closest)
    return closest