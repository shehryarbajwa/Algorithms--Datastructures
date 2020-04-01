import unittest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #Average O(log n) time O(1) space
    #worst o(n) time O(1) space
    #Worst is when there is a straight line
    def insert(self, value):
        currentNode = self

        while True:
            if value < currentNode.value:
                if currentNode.left == None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            
            else:
                if currentNode.right == None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    #Average O(logn) time O(1) space
    #Worst O(n) time O(1) space
    def contains(self, value):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            
            elif value > currentNode.value:
                currentNode = currentNode.right

            else:
                return True
        return False

    #Average O(log n) time O(1) space
    #Worst O(n) time | O(1) space
    def remove(self, value, parentNode = None):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left

            elif value > currentNode.value:
                parentNode = currentNode.right
                currentNode = currentNode.right

            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.find_min_value()
                    value_to_remove = currentNode.value
                    currentNode.right.remove(value_to_remove, currentNode)
                
                if parentNode is None:
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

                elif parentNode.left == currentNode:
                    if currentNode.left is None and currentNode.right is None:
                        parentNode.left = None
                    else:
                        parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                
                elif parentNode.right == currentNode:
                    if currentNode.right is None and currentNode.left is None:
                        parentNode.right = None
                    else:
                        parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self


    def find_min_value(self):
        currentNode = self

        while currentNode.left is not None:
            currentNode = currentNode.left

        return currentNode.value


def in_order_traversal(node, array):

    #Tree is not a leaf node
    if node is not None:
        in_order_traversal(node.left, array)
        array.append(node.value)
        in_order_traversal(node.right, array)
    return array

def pre_order_traversal(node, array):

    if node is not None:
        array.append(node.value)
        pre_order_traversal(node.left, array)
        pre_order_traversal(node.right, array)
    return array

def post_order_traversal(node, array):
    
    if node is not None:
        post_order_traversal(node.left, array)
        post_order_traversal(node.right, array)
        array.append(node.value)
    return array

class Tests(unittest.TestCase):
    def test_case_1(self):
        node_1 = BST(10).insert(5).insert(15).insert(2).insert(5).insert(1).insert(22)
        self.assertEqual(post_order_traversal(node_1, []), [1, 2, 5, 5, 22, 15, 10])

    def test_case_2(self):
        node_1 = BST(10).insert(5).insert(15).insert(2).insert(5).insert(1).insert(22)
        self.assertEqual(pre_order_traversal(node_1, []), [10, 5, 2, 1, 5, 15, 22])
    
    def test_case_3(self):
        node_1 = BST(10).insert(5).insert(15).insert(2).insert(5).insert(1).insert(22)
        self.assertEqual(in_order_traversal(node_1, []), [1, 2, 5, 5, 10, 15, 22])


if __name__ == "__main__":
    unittest.main()
