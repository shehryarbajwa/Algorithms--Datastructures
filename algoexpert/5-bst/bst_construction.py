class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #Average O(logn) time O(1) space
    #Worst O(n) time O(1) space
    def insert(self,value):
        current_node = self
        while True:
            if value < current_node.value:

                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                current_node = current_node.right
        return self

    #Average O(logn) time O(1) space
    #Worst O(n) time O(1) space
    def contains(self, value):
        current_node = self
        while current_node is not None:
            
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False

    #Average O(logn) time O(1) space
    #Worst O(n) time O(1) space
    def remove(self, value, parentNode = None):
        current_node = self

        while current_node is not None:
            if value > current_node.value:
                parentNode = current_node
                current_node = current_node.right
            elif value < current_node.value:
                parentNode = current_node
                current_node = current_node.left
            else:
                #Case 1 - Node has two children
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_right_value()
                    current_node.right.remove(current_node.value, current_node)

                #Case 2 - Node has 1 child but no parent. Root node with 1 child
                #Root node with 2 children has been discussed
                elif parentNode is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left

                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.right = current_node.right.right
                        current_node.left = current_node.right.left
                    #Single node tree no left or right child
                    else:
                        pass
                
                elif parentNode.left == current_node:
                    parentNode.left = current_node.left if current_node.left is not None else current_node.right
                
                elif parentNode.right == current_node:
                    parentNode.right = current_node.right if current_node.right is not None else current_node.left

                break
        return self

    def get_min_right_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    

    