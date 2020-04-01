
# A node is said to be a BST, if and only if satisfies the BST property. Its value is less than or equal to the values of every node to its right



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #Iteratively
    #Average O(logn) Time and O(1) space complexity
    def insert(self, value):
        current_node = self

        #Our loop stops once we have inserted a value
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    break
                #If currentNode is not none, we update the currentNode
                else:
                    current_node = current_node.left
            elif value == current_node.value:
                if current_node.right is None:
                    current_node.right = Node(value)
                    break
                else:
                    current_node = current_node.right
            else:
                return "Node with the `{value}` has already been inserted in the tree"
        #Return self so we can call insert one after another when we test the algorithm
        #testBst.insert(1).insert(1).insert(1) so we can chain these together
        return self

        #                10
        #              /    \
        #            7       13
        #           / \      /  \
        #          4   8    12   22
        # Find if the BST contains 12
    def contains(self, value):
        #Current node is root node
        currentNode = self

        #While the currentNode is not empty
        #When currentNode becomes 12, we can see value = currentNode.value so we return True
        while currentNode is not None:
            #If 12 < 10, we move to the left otherwise to the right
            #If 12 < 13, we move to the left
            #Currentnode becomes 12
            if value < currentNode.value:
                currentNode = currentNode.left
            #Since 12 is > 10, we move to the right
            #currentNode becomes 13
            elif value > currentNode.value:
                currentNode = currentNode.right
            #else value == currentNode
            # if value == currentNode.value:
            #     return True
            else:
                return True
        return False

    def remove(self, value, parentNode = None):
        currentNode = self

        while currentNode is not None:
            #Compare value
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.get_min_value()
                    value_to_remove = currentNode.value
                    currentNode.right.remove(value_to_remove, currentNode.right)
                
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right

                    else:
                        currentNode.value = None


                #         Remove a node that doesnt have two children nodes - It could be either 1 child node or None
                #         Then check if the node to remove has a left child or a right child
                #         
                #                       3
                #                     /   \
                #                    1     5
                #                   / \   /  \
                #                  0  2  4    6
                #                 /
                #               -0.5
                #                   Remove 0
                #                   Current Node is 0
                #                   Parent node is 1
                #                   In this case, we assign 1's left to 0's left if it exists otherwise 1's right

                elif parentNode.left == currentNode:
                    if currentNode.left is None and currentNode.right is None:
                        parentNode.left = None
                    else:
                        #If there exists a child on either left or right side
                        #If it exists on the left side, we can assign it as the left child of the parent Node
                        #If it exists on the right side, we can assign it as the left child of the parent Node since there are no two children nodes
                        parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right


                #                        3
                #                      /    \
                #                     1       5
                #                   /  \     /  \
                #                   0   2   4    6
                #                      /  \
                #                   1.99   2.5
                #                   Current Node is 2
                #                   Parent Node is 1
                #                   We assign 1's right to 2.5
                #If there exists a child on either right or left side

                elif parentNode.right == currentNode:
                    #If there exists no child on left or right. Then we assign parentNode's right to None
                    if currentNode.right is None and currentNode.left is None:
                        parentNode.right = None
                    #If there does exist a value on either sides left or right
                    #If it exists on the left side, we assign the left side since it satisfies the property of the child node being larger than parentNode
                    #If it exists on the right side, we assign the right side since there is no left
                    else:
                        parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right


    def get_min_value(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

                

                


    





    

    




