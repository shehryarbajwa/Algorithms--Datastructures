#Function that takes in a binary tree and for each left node in the tree, it should
#swap it with every mirrored right node
# A naive approach would be to traverse the tree. At each traversal, append to array the left and the right and stop.
# If you do a depth first search, then swap each element first before moving on to leaves.

#Steps:
# 1- Take the root node. We start at root and go level by level in a breadth first fashion
# 2- Then for the root node's children, swap them.
# 3- After swap, add the left child and right child to the queue
# 4- The pointers of the children nodes remain constant and will have kept their original pointers intact.
# 5- When a node has children that are both None, add them to the queue.
# 6- When we reach a Null node, we use python's continue function to go back to while loop.
# 7- While loop stops when len(queue) = 0.

# Space Complexity will be O(N) because at one point, all leaf nodes will be saved in the queue.
# That will include all null nodes.


#Iterative solution
# Time Complexity O(N)
# Space Complexity O(N)

def invertBinaryTree(tree):

    queue = [tree]

    while len(queue) > 0:
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftandRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftandRight(tree):
    tree.left, tree.right = tree.right, tree.left


# Recursive Algorithm

# Time Complexity O(N)
# Space Complexity O(d) d is the height of the tree

def invertBinaryTreeRecursively(tree):
    #Base case. Reach leaf node

    if tree is None:
        return
    swapLeftandRightRecurive(tree)
    invertBinaryTreeRecursively(tree.left)
    invertBinaryTreeRecursively(tree.right)

def swapLeftandRightRecurive(tree):
    tree.left, tree.right = tree.right, tree.left