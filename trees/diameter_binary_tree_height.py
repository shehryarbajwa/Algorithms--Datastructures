# The diameter of a tree T is the largest of the following quantities:

# * the diameter of T’s left subtree
# * the diameter of T’s right subtree
# * the longest path between leaves that goes through the root of T (this can be computed from the heights of the subtrees of T)

# Diameter of a Tree - It is the longest path between two nodes in a a tree 

# The question to ask the interviewer is do we count the node itself in calculating the subtree
# For assumption, we will count the node itself
# If we dont want to count the node itself, just return max of lheight + rheight and max of ldiameter and rdiameter


class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
  
""" 
The function Compute the "height" of a tree. Height is the  
number f nodes along the longest path from the root node  
down to the farthest leaf node. 
"""
def height(node): 
      
    # Base Case : Tree is empty 
    if node is None: 
        return 0
      
    # If tree is not empty then height = 1 + max of left  
    # height and right heights  
    return 1 + max(height(node.left) ,  height(node.right)) 



  
# Function to get the diamtere of a binary tree 
def diameter(root): 
      
    # Base Case when tree is empty  
    if root is None: 
        return 0; 
  
    # Get the height of left and right sub-trees 
    lheight = height(root.left) 
    rheight = height(root.right) 
  
    # Get the diameter of left and right sub-trees 
    ldiameter = diameter(root.left) 
    rdiameter = diameter(root.right) 
  
    # Return max of the following tree: 
    # 1) Diameter of left subtree 
    # 2) Diameter of right subtree 
    # 3) Height of left subtree + height of right subtree + 1  
    return max(lheight + rheight + 1, max(ldiameter, rdiameter)) 

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(3)
root.right.right = Node(6)
print ("Diameter of given binary tree is %d" %(diameter(root)))


#Lets start with an example
# We have a tree with root 1, left node 2 and right node 3
# The diameter is 3


#diameter 
#   We start with diameter of root(1) - > 
#   diameter(1)
#   Calculate the height of the left subtree
#   lheight = height(1.left)
    #   height(2)
    #       height(2)
    #       return 1 + max(height(node.left == 3), height(node.right == None))
    #       height(3)
    #       return 1 + max(height(3.left == None), height(3.right == None))
    #       1 + max(0, 0) -> 1
#   height(2)
#   return 1 + max(1, 0) -> 1 + 1 -> 2
#   lheight becomes 2
#   rheight(1.right == 3)
    #   height(3)
    #       height(3)
    #       return 1 + max(height(3.left == None), height(3.right == 6))
    #       height(6)
    #       return 1 + max((6.left == None), height(6.right == None))
    #       return 1 + max(0,0) -> 1
    #   height(3)
#   return 1 + max(0, 1) -> 2
#   back to diameter(1)
#   lheight is 2
#   rheight is 2
#   ldiameter is diameter(root.left)
#   ldiameter = diameter(2)
    #       diameter(2)
    #       lheight = height(2.left == 3)
    #       lheight = 1
    #       rheight = height(2.right == None) = 0
    #       ldiameter = (2.left == 3)
#       ldiameter(3)
#       lheight = height(3.left == None) -> 0
#       rheight = height(3.right == None) -> 0
#       rdiameter = 0
#       return max(1,0) -> 1
#       ldiameter(3) -> 1
#     diameter(2)
#     rdiameter(2.right == None) -> 0
#     return max(1 + 1 + 0, max(ldiameter, rdiameter == 0))
#     return max(2, max(1,0))
#     diameter(2) returns 2
#   diameter(1)
#   lheight = 2
#   rheight = 2
#   ldiameter = 2
#   rdiameter = diameter(1.right == 3)
#   diameter(3)
    #   lheight = 0
    #   rheight = (3.right == 6)
    #   rheight = height(6)
    #   height(6) return 1 + max(0,0) -> 1
    #   height(6) returns 1
    #   rheight = 1
    #   ldiameter = diameter(3.left) -> 0
    #   rdiameter = diameter(3.right) -> diameter(6)
    #       diameter(6)
    #       lheight = 0
    #       rheight = 0
    #       ldiameter = 0
    #       rdiameter = 0
    #       return 1
    #  rdiameter returns 1
    #  diameter(3)
    #  return max(1 + 0 + 1, max(0, 1))
    #  diameter(3) returns 2
    #  rdiameter = 2
    #  diameter(1)
    #  lheight = 2
    #  rheight = 2
    #  ldiameter = 2
    #  rdiameter = 2
    #  return max(1 + 2 + 2, max(2,2))
    # return 5
    # diameter(root) returns 5



# Here is the strategy
# 1-We create a diameter function
# 2-It takes  in the root node
# 3-It finds the hieght of the left subtree
# 4-It finds the height of the right subtree
# 5-It then finds the left diameter of the subtree - i.e from getting from leaf to root node
# 6-It then finds the right diameter of the subtree - i.e from getting from leaf to root node
# 7-Then we calculate the maximum of either these 3:
#   1-diameter of left subtree
#   2-diameter of right subtree
#   3-the longest path between leaves that goes through the root of T (this utilizes the height function)

