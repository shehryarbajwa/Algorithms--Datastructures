# Given the root of a binary tree, find the diameter

# Diameter of a binary tree is the maximum distance between any two nodes
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# In the example below, Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3]

    #      1
    #      / \
    #     2   3
    #    / \     
    #   4   5  


class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

from queue import Queue

#We can convert our array to a binary tree
#The array we have is [1, 2, 3, 4, 5, None, None, None, None, None, None]



def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree 
    """

    #Start at index 0
    index = 0
    length = len(arr)
    
    if length <= 0 or arr[0] == -1:
        return None

    #Get the root which is a node at arr index 0
    root = BinaryTreeNode(arr[index])
    #increment index by 1
    index += 1
    #Create a queue
    queue = Queue()
    #Add an element to the queue
    queue.put(root)
    #In 1st iteration, queue has 1 as its only element


    #Since queue has 2 elements 2 and 3
    #We will continue while loop again with 2nd iteration
    
    

    #While the queue is not empty, keep running the while loop
    while not queue.empty():
        #Queue is FIFO, so we current node becomes 1
        
        #2nd iteration current_node becomes 2
        #Queue now only has 1 element which is 3
        current_node = queue.get()
        #Left child is arr[1] -> 2

        #2nd iteration left child becomes arr[3] -> 4
        left_child = arr[index]
        #Increment the index
        
        #Second iteration, incremenet index by 1, now index is 4
        index += 1
        
        #If the left child is not None
        if left_child is not None:
            #Left node becomes BinaryTreeNode

            #Left node becomes new node
            left_node = BinaryTreeNode(left_child)
            #Current node's left pointer now leads to the left node which is 2 so 1 has left node of 2
            current_node.left = left_node
            #Add 2 to queue. Queueu is 2 now
            queue.put(left_node)
        
        #We then search for right_child which is arr[2] -> 3
        #Increment index by 1
        right_child = arr[index]
        index += 1

        #If right child is not None
        
        if right_child is not None:
            #Create a right node
            right_node = BinaryTreeNode(right_child)
            #Current node's right pointer is 3 now 1 has left node of 2 and right node of 3
            current_node.right = right_node
            #Add 3 to queue
            queue.put(right_node)
    return root


def diameter_of_binary_tree(root):
    return diameter_of_binary_tree_func(root)[1]

def diameter_of_binary_tree_func(root):
    #For example, our tree is 1 left node 2 and right node 3
    #Arr = [1,2,3]

    #We start with the root, which is 1
    #We calculate left_height,left_diameter which will run as follows

    #   first function is diameter_of_binary_tree_func(1)
    #   1.left    diameter_of_binary_tree_func(2)
    #   2.left      diameter_of_binary_tree_func(None) -> returns 0,0
    #             Going one step back, we get diameter_of_binary_tree_func(2)
    #             We iterate, right_height is None, so right_height, right_diameter is 0,0
    #             current_height becomes max(0,0) + 1 -> 1
    #             height diameter becomes 0 + 0 - > 0
    #             current_diameter becomes max(0, 0, 0) -> 0
    #             We return diameter_of_binary_tree_func(2) as 1,0
    #   Now back to diameter_of_binary_tree_func(1)
    #   left_height, left_diameter is 1,0
    #   right_height,right_diameter we run diameter_of_binary_tree_func(3)
    #       diameter_of_binary_tree_func(3) -> left_height is 0,0
    #       right_height, right_diameter becomes diameter_of_binary_tree_func(5)
    #           diameter_of_binary_tree_func(5) -> returns 
    #           diameter_of_binary_tree_func(5)
    #               right_height, right_dia returns 0,0
    #               current_height becomes max(0,0) + 1
    #               height diameter becomes 0
    #               current_diameter becomes max()
    
    #   We recurse back to diameter_of_binary_tree_func(3)
    #   3's left height, left diameter is 0,0
    #   3's right_height, right_diameter is 0,0
    #   

    if root is None:
        return 0,0

    left_height, left_diameter = diameter_of_binary_tree_func(root.left)
    #Recursively, in the first attempt, it goes down to 0,0
    right_height, right_diameter = diameter_of_binary_tree_func(root.right)
    #Recursively, in the first attempt, it goes down to 0,0

    #Current height becomes max(0,0) + 1 -> 1
    #height diameter = 0 + 0 -> 0
    #Current_diameter = max(0,0,0) -> 0
    #In the first recursion we return 1, 0
    current_height = max(left_height, right_height) + 1
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)

    return current_height, current_diameter



    
arr = [1, 2, 3, None, None, None, None]
root = convert_arr_to_binary_tree(arr)

print(diameter_of_binary_tree(root))
