# Insight is each time the difference between the currentNode's value vs 
# the targetValue is smaller than difference between the target value and 
# set closest value, we need to update the closest value

#Average Time Complexity: O(logn)
#Average Space Complexity: O(1)

#Worst case: Time Complexity: O(n)
#Worst case: Space Complexity: O(1)

#Average time is when we can split the tree in half and store only 2 variables the currentNode and closest value so space complexity is O(1)
#Worst time is when the tree is branch shaped and we have to traverse through the entire tree and not split in half

def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, tree.value)

def findClosestValueInBSTHelper(tree, target, closest):
    currentNode = tree

    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        
        if target < currentNode.value:
            currentNode = currentNode.left
        
        if target > currentNode.value:
            currentNode = currentNode.right

        else:
            break
    return closest