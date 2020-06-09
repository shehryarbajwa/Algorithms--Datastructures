

#Time Complexity O(N)
#Space Complexity O(D) for d frames on the call stack
def binary_tree_invert(tree):

    return binary_tree_invert_helper(tree)

def binary_tree_invert_helper(tree):
    current_node = tree

    if current_node is None:
        return
    
    swap(current_node)
    binary_tree_invert_helper(current_node.left)
    binary_tree_invert_helper(current_node.right)

def swap(current_node):
    current_node.left, current_node.right = current_node.right, current_node.left


#Iterative algorithm
# Time Complexity O(N)
# Space Complexity O(N) - Roughly N/2 nodes in queue if tree is balanced and almost half nodes at leaf level
def invert_binary_tree(tree):
    queue = [tree]

    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node is None:
            continue
        swap(current_node)
        queue.append(current_node.left)
        queue.append(current_node.right)
