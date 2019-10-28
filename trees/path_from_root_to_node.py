# Given the root of a Binary Tree and a data value representing a node, return the path from the root to that node in the form of a list. 
# You can assume that the binary tree has nodes with unique values.

from queue import Queue
class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def convert_arr_to_binary_tree(arr):

        index = 0
        length = len(arr)

        if length <= 0 or arr[0] == =1:
            return None
        
        root = BinaryTreeNode(arr[index])
        index += 1
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            current_node = queue.get()
            left_child = arr[index]
            index += 1

            if left_child is not None:
                left_node = BinaryTreeNode(left_child)
                current_node.left = left_node
                queue.put(left_node)

            right_child = arr[index]
            index += 1

            if right_child is not None:
                right_node = BinaryTreeNode(right_child)
                current_node.right = right_node
                queue.put(right_node)

        return root

    def path_from_root_to_node(root, data):
        output = path_from_node_to_root(root, data)
        return list(reversed(output))

    def path_from_node_to_root(root, data):
        #We start with 1 as root and data to be 3
        #The Tree is with root 1
        #Root's left child 2
        #Root's left.left child 3

        
        if root is None:
            return None
            
        #If the root.data is 1 and the value we need to find is 3
        # So we have a tree with root 1.
        # Root's left child is 2
        # 2's left child is 3
        elif root.data == data:
            return [data]

        left_answer = path_from_node_to_root(root.left, data)
        #Left answer is not None only when we root.data == data
        #In that case the value of left answer is [data]
        if left_answer is not None:
            #So we had [3]
            left_answer.append(root.data)
            return left_answer

        right_answer = path_from_node_to_root(root.right, data)
        if right_answer is not None:
            right_answer.append(root.data)
            return right_answer
        return None

#In the first iteration, we reach left_answer and we run path_from_node_to_root(1.left == 2, 3)
#We keep going since root.data == 2 != 3, we continue
#We reach left_answer again path_from_node_to_root(2.left == 3, 3)
#since root.data == data, we return [3]

#path_from_node_to_root(3,3) -> [3]
#We are back in path_from_node_to_root(2,3)
#Since left_answer is not None, we append root.data to [3] it becomes [3,2]
#Back to path_from_node_to_root(1,3)
#left_answer is [3,2]
#Since left_answer is not None
#We append and it becomes [3,2,1]
#We then reverse it 
#It becomes [1,2,3]
#The path from the root to the node is 1 -> 2 -> 3