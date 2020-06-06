class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

#Time Complexity O(N log n) - Inserting elements takes log n and we are inserting n elements
#Space Complexity O(N) - Inserting N elements
def construct_min_bst(array):
    return construct_min_bst_helper(array, None, 0, len(array) - 1)

def construct_min_bst_helper(array, bst, startIdx, endIdx):
    if startIdx > endIdx:
        return

    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    construct_min_bst_helper(array, bst, startIdx, midIdx - 1)
    construct_min_bst_helper(array, bst, midIdx + 1, endIdx)
    return bst

def construct_min_bst(array):
    return construct_min_bst_helper(array, None, 0, len(array) - 1)

def construct_min_bst_helper(array, bst, startIdx, endIdx):
    if startIdx > endIdx:
        return

    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    construct_min_bst_helper(array, bst, startIdx, midIdx - 1)
    construct_min_bst_helper(array, bst, midIdx + 1, endIdx)
    return bst

#Time complexity O(N) - since we are providing the left and subtree root nodes and manually inserting them
#Space Complexity O(N)
def construct_min_bst(array):
    return construct_min_bst_helper(array, None, 0, len(array) - 1)

def construct_min_bst_helper(array, bst, startIdx, endIdx):
    if startIdx > endIdx:
        return

    midIdx = (startIdx + endIdx) // 2
    newbstNode = BST(array[midIdx])
    if bst is None:
        bst = newbstNode
    else:
        if array[midIdx] < bst.value:
            bst.left = newbstNode
            bst = bst.left
        else:
            bst.right = newbstNode
            bst = bst.right
    construct_min_bst_helper(array, bst, startIdx, midIdx - 1)
    construct_min_bst_helper(array, bst, midIdx + 1, endIdx)
    return bst

def minHeightBst(array):
    return construct_min_bst_helper(array, None, 0, len(array) - 1)

def construct_min_bst_helper(array, bst, startIdx, endIdx):
    if startIdx > endIdx:
        return

    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
	bst.left = construct_min_bst_helper(array, bst, startIdx, midIdx - 1)
    bst.right = construct_min_bst_helper(array, bst, midIdx + 1, endIdx)
    return bst