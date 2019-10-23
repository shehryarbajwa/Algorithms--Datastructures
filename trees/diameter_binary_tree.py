# Given the root of a binary tree, find the diameter

# Diameter of a binary tree is the maximum distance between any two nodes
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# In the example below, Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3]

    #      1
    #      / \
    #     2   3
    #    / \     
    #   4   5  

from queue import Queue

class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def convert_arr_to_binary_tree(arr):
    #The above example would be represented by [1,2,3,4,5,None,None,None,None,None,None]

    index = 0
    length = len(arr)

    if length <= 0 or arr[0] == -1:
        return None

    
    #Root becomes arr[0] -> 1
    #We increment the index by 1
    #We create an empty queue
    #Remember queue is FIFO
    #We add root to the queue
    #Queue is now 1

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)

    # First iteration of while loop done
    # Queue is now 2,3
    # In the second iteration, since 2 was added first, we start with 2 and get current_node
    # Once we get current_node we then get the left child of the current_node
    # 


    #While the queue is not empty, which means as long as queue has items in it
    #While queue has items in it, keep running the loop
    while not queue.empty():
        #Queue.get will return the item from the queue
        #That is how we get current_node
        # Current node becomes 1
        current_node = queue.get()
        print(queue.get())
        #Left child becomes arr[1] -> 2
        ## In the second it, left_child becomes 
        left_child = arr[index]
        index += 1

        if left_child is not None:
            #  Since left child is None, we traverse
            #  Left_node becomes a new node with the value of the left child which is 2
            #  Current node is 1 and its left pointer now leads to left_node which is 2
            #  We add left_node to queue
            #  Queue becomes 2

            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)

        #Right child is arr[2] -> 3
        right_child = arr[index]
        #index is now 3
        index += 1

        if right_child is not None:
            #Since right child is a value, we traverse
            #We create a right_node with __init__ providing data as rightChild which is 3
            #Then we create the right pointer for the current node which is 1 so it leads to 3
            #We then add this to the queue
            #Queue becomes [2,3]
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root

def diameter_of_a_binary_tree(root):
    return diameter_of_a_binary_tree_func(root)[1]

def diameter_of_a_binary_tree_func(root):

    if root is None:
        return 0,0

    left_height, left_diameter = diameter_of_a_binary_tree_func(root.left)
    right_height, right_diameter = diameter_of_a_binary_tree_func(root.right)

    current_height = max(left_height, right_height) + 1
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)

    return current_height, current_diameter






