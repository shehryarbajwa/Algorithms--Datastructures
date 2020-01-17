
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self

        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left

            elif value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def validateBstHelper(currentNode, minimum, maximum):
        # Two subcases
        # Subcase 1: Maximum value for left is root node
        # Subcase 2: Minimum value for right subtree is root node

        # Base case: When you reach the leafs

        # Edge case: When root has no children

        if currentNode is None:
            return True

        if currentNode.value < minimum or currentNode.value >= maximum:
            return False

        # Right side
        # When the currentNode's value is greater than or equal to the root value

        # Subcase 1
        leftSide = left_Side(currentNode.left, minimum, currentNode.value)
        # Subcase 2
        rightSide = right_Side(currentNode.right, currentNode.value, maximum)

        return leftSide and rightSide

    def left_Side(leftNode, minimum, parentNode):

        if leftNode is None:
            return True

        if leftNode.value >= parentNode:
            return False

        if leftNode.value < minimum:
            return False

    def right_Side(rightNode, parentNode, maximum):

        if rightNode is None:
            return True

        if rightNode.value <= parentNode:
            return False

        if rightNode.value < maximum:
            return False

    def validateBST(self, tree):
        return validateBstHelper(tree, float('-inf'), float('inf'))

BST_1 = BST(10).insert(5).insert(15)


print(BST_1.validateBST(10))