# This is an input class. Do not edit.
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

#Time Complexity O(N) since we have to traverse once
#Space Complexity O(N) due to recursive calls being saved in the call stack
def validateBst(tree):
    return validateBSThelper(tree, float('-inf'), float('inf'))

def validateBSThelper(currentNode, minimum, maximum):
	
	if currentNode is None:
		return True
	print('Got here')
	leftSide = leftSideHelper(currentNode.left, minimum, currentNode.value)
	rightSide = rightSideHelper(currentNode.right, currentNode.value, maximum)
	return leftSide and rightSide

def leftSideHelper(leftNode, minimum, parentNode):
    print(leftNode.value)
    print('Parent node is', parentNode)
    if leftNode is None:
        return True

    if leftNode.value >= parentNode:
        return False
    elif leftNode.value < minimum:
        return False
    else:
        return True
	
def rightSideHelper(rightNode, parentNode, maximum):
    print(rightNode.value)
    print('Parent node is', parentNode)
    if rightNode is None:
        return True

    if rightNode.value <= parentNode:
        return False

    elif rightNode.value > maximum:
        return False
    else:
        return True
	

BST_1 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22)
print(validateBst(BST_1))