# # Construct a binary search tree with left values smaller than root and right values > root

# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     #Average O(logn) eliminating half of the tree
#     #Worst case O(N) when a straight tree
#     #Average Case: Space Complexity O(logn) if done recursively
#     #Worst Case: Space Complexity O(N) if done recursively
#     #Space Complexity O(1) if done iteratively

#     def insert(self, value):
#         if value < self.value:
#             if self.left is None:
#                 self.left = BST(value)
#             else:
#                 self.left.insert(value)

#         if value > self.value:
#             if self.right is None:
#                 self.right = BST(value)
#             else:
#                 self.right.insert(value)
#         return self

#     #Average O(logn) eliminating half of the tree
#     #Worst case O(N) when a straight tree
#     #Average Case: Space Complexity O(logn) if done recursively
#     #Worst Case: Space Complexity O(N) if done recursively
#     #Space Complexity O(1) if done iteratively
#     #Return a boolean value indicating whether the value is present in the BST
#     def search(self, value):

#         if value < self.value:
#             if self.left is None:
#                 return False
#             else:
#                 return self.left.search(value)
        
#         elif value > self.value:
#             if self.right is None:
#                 return False
#             else:
#                 return self.right.search(value)
#         #else if value == self.value return True
#         else:
#             return True
    
#     #Edge cases
#     #1- If the value to remove is a leaf, remove the value by setting to Null.
#     #2- If the value has one child node, remove the value and set child node to be parent Node.
#     #3- If the value has two children nodes, then find the smallest value in the right-subtree of the removed value and replace it
#     #   This way we maintain the binary search tree properties of left and right values.
#     #   By default the smallest value will be a leaf node
#     #   

#     #Average O(logn) eliminating half of the tree
#     #Worst case O(N) when a straight tree
#     #Average Case: Space Complexity O(logn) if done recursively
#     #Worst Case: Space Complexity O(N) if done recursively
#     #Space Complexity O(1) if done iteratively
#     def remove(self, value):

#         if value < self.value:



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

    def contains(self, value):
        currentNode = self

        while currentNode is not None:
            if value > currentNode.value:
                currentNode = currentNode.right

            elif value < currentNode.value:
                currentNode = currentNode.left
            elif value == currentNode.value:
                return True
            else:
                return False
        return self

    def remove(self, value, parentNode=None):
        currentNode = self

        while currentNode is not None:
            if value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                #subcase 1: if node has no children
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.get_min_value()
                    currentNode.right.remove(currentNode.value, currentNode)
                
                #subcase 2: if node has one children
                #If node removed has one child
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.left = currentNode.left.left
                        currentNode.right = currentNode.left.right

                    if currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.right = currentNode.right.right
                        currentNode.left = currentNode.right.left

                    else:
                        currentNode.value = None
                elif parentNode.left is currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right is currentNode:
                    parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
                break
        return self

    def get_min_value(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value




    # 5
#   /   \
#  3     7
# /        \
#1          9

                



            


