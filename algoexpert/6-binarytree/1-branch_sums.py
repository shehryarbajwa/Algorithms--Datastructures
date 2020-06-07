class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#Time Complexity O(N)
#Space Complexity O(N) - 1-frames on the call stack
#At most in a binary tree, we can have n/2 leaf nodes
#We are bounded by O(n) as upper bound - if we have a perfectly balanced binary tree
def branch_sums(root):
    sums = []
    branch_sums_helper(root, 0, sums)
    return sums

def branch_sums_helper(node, runningsum, sums):

    if node is None:
        return
    current_sum = runningsum + node.value

    if node.left is None and node.right is None:
        sums.append(current_sum)
        return

    branch_sums_helper(node.left, current_sum, sums)
    branch_sums_helper(node.right,current_sum, sums)
    


bt = BinaryTree(1)
bt.left = BinaryTree(2)
bt.right = BinaryTree(3)
bt.left.left = BinaryTree(4)
bt.left.right = BinaryTree(5)
bt.right.left = BinaryTree(6)
bt.right.right = BinaryTree(7)
bt.left.left.left = BinaryTree(8)
bt.left.left.right = BinaryTree(9)
bt.left.right.left = BinaryTree(10)

print(branch_sums(bt))


