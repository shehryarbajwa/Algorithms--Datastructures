
import unittest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

class Tests(unittest.TestCase):
    def test_case_1(self):
        node_1 = BST(10).insert(8).insert(12)
        self.assertEqual(node_1.contains(12), True)

    def test_case_2(self):
        node_1 = BST(10).insert(8).insert(12)
        self.assertEqual(node_1.contains(13), False)

    def test_case_3(self):
        node_1 = BST(10).insert(8).insert(12)
        self.assertEqual(node_1.left.value, 8)

    def test_case_4(self):
        node_1 = BST(10).insert(8).insert(12).insert(6).insert(9).insert(11).insert(13)
        self.assertEqual(node_1.right.value, 12)

    def test_case_5(self):
        node_1 = BST(10).insert(8).insert(12).insert(6).insert(9).insert(11).insert(13).insert(12.5)
        node_1.remove(12)
        self.assertEqual(node_1.right.value, 12.5)




if __name__ == '__main__':
    unittest.main()
                    