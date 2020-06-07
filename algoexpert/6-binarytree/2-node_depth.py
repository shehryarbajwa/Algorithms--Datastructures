class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



#Time Complexity O(N)
#Space Complexity O(d) at most on stack there will be elements the size of the largest tree
def node_depth_iterateive(root):
    runningsum = 0
    stack = [{"node":root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumofdepth += depth
        stack.append({"node":node.left, "depth": depth + 1})
        stack.append({"node":node.right, "depth": depth + 1})
    return sumofdepth

#Time Complexity O(N)
#Space Complexity O(d) for having at most d frames on the call stack
def node_depth_recursive(root, depth = 0):
    if root is None:
        return 0
    return depth + node_depth_recursive(root.left, depth + 1) + node_depth_recursive(root.right, depth + 1)


def node_depth(root):
    nodes_depth = []
    node_depth_helper(root, 0, nodes_depth)

    return sum(nodes_depth) - 1

def node_depth_helper(node, runningsum, nodes_depth):

    if node is None:
        return

    runningsum += 1

    if node.left is None and node.right is None:
        nodes_depth.append(runningsum)
        return
    node_depth_helper(node.left, runningsum, nodes_depth)
    node_depth_helper(node.right, runningsum, nodes_depth)

bt = BinaryTree(1)
bt.left = BinaryTree(2)
bt.right = BinaryTree(3)
bt.left.left = BinaryTree(4)
bt.left.right = BinaryTree(5)
bt.right.left = BinaryTree(6)
bt.right.right = BinaryTree(7)
bt.left.left.left = BinaryTree(8)
bt.left.left.right = BinaryTree(9)

print(node_depth(bt))

