
class BinarySearch:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

## Time Complexity O(N) since we traverse each node in the Binary Tree
## Space Complexity O(N) since at most our branch sum will not be more than N

## It could be O(logn) if we could skip half the tree like finding a target number
## But since we cannot skip the tree and have to calculate each branch sum, it is O(N)


## And recursive functions have leaf node which are almost half of N
## At leaf we have around half the nodes of the tree
## Therefore saving those nodes in memory requires O(N/2) which is O(N) space complexity


def branchSum(root):
    sums = list()
    depth_first_search(root, 0, sums)
    return sums

def depth_first_search(node, runningSum, sums):
    
    if node is None:
        return

    NewrunningSum = runningSum + node.value

    if node.left and node.right is None:
        sums.append(NewrunningSum)
        return

    depth_first_search(node.left, NewrunningSum, sums)
    depth_first_search(node.right, NewrunningSum, sums)

    