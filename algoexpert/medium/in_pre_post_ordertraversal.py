#                             10
#                           /   \
#                         5       15
#                       /  \        \
#                      2    5       22
#                    /       \      / \
#                   1         6    20  24  

# In-order = [1,2,5,5,6,10,15,20,22,24]
# In in-order, we first get to the left basecase which are the leafs.
# Then we append the currentValue and then traverse on the right side

# We start with 10 -> 5 -> 2 -> 1 -> [1]
# We come back up, since we have appended and no right value for 2 so [1,2]
# We come back up, 5's left is [1,2] and now current value is 5 so [1,2,5]
# 5's right there is no left so we append 5 and then append 6 [1,2,5,5,6]
# Come back up again at 10's left is [1,2,5,5,6] so [1,2,5,5,6,10]
# Recurse on 10's right -> 15
# 15 has no left so append 15
# Recurse 15's right so [1,2,5,5,6,10,15]
# 22 has left so we get 20 first [1,2,5,5,6,10,15,20]
# Then go back since 20 is leaf.
# 22's left is [20]
# Then append 22's current value
# [1,2,5,5,6,10,15,20,22]
# Finally we recurse to the right [1,2,5,5,6,10,15,20,22,24]
# We run this tree is not None
# Once we finish we return array



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        
        currentNode = self

        if value > currentNode.value:
            if currentNode.right is None:
                currentNode.right = BST(value)
            else:
                currentNode.right.insert(value)
        elif value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = BST(value)
            else:
                currentNode.left.insert(value)

        return self
        


def in_order_traversal(tree, array):
    if tree is not None:
        in_order_traversal(tree.left, array)
        array.append(tree.value)
        in_order_traversal(tree.right, array)
    else:
        return 
    
    return array

#                             10
#                           /   \
#                         5       15
#                       /  \        \
#                      2    5       22
#                    /       \      / \
#                   1         6    20  24  

# Pre-order we start with root.
# Then recurse left and then right
# [10, 5, 2, 1, 5, 6, 15, 22, 20, 24 ]
def pre_order_tree(tree, array):
    if tree is not None:
        array.append(tree.value)
        pre_order_tree(tree.left, array)
        pre_order_tree(tree.right, array)
    else:
        return 

    return array

#[1,2,6,5,5,20, 24, 22, 15,10]
def post_order_tree(tree, array):
    if tree is not None:
        post_order_tree(tree.left, array)
        post_order_tree(tree.right, array)
        array.append(tree.value)

    else:
        return 
    
    return array

#                           /   \
#                         5       15
#                       /  \        \
#                      2    5       22
#                    /       \      / \
#                   1         6    20  24  
#In-order means in the middle add to array
#Pre-order means add it to the array before recursing left or right
#Post-order means add it to the array after recursing left and right

BST_1 = BST(10).insert(5).insert(2).insert(5).insert(1).insert(6).insert(15).insert(22).insert(20).insert(24)

print(post_order_tree(BST_1, []))