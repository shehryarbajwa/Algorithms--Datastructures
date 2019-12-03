### Red black tree rules
### 1-All nodes have a color
### 2-All nodes have two children (use NULL nodes)
### 3-All null nodes are colored black
### 4-If a node is red, its children must be black
### 5-The root node must be black
### 6-Every path to its descendant NULL nodes must contain the same number of black nodes

class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

class RedBlackTree(object):
    def __init__(self, root):
        #Insert the root node
        #self.root = Node(value=root, parent=None, 'red')
        self.root = Node(root, None, 'red')
    
    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    def insert_helper(self, current, new_val):
        #Current denotes the root node
        #if root.value < new_inserted_value
        #example root is 8
        #inserted value is 7
        #since root value is > new_val
        #We move to else statement
        #if current.left exists, we do recursion with the current.left's value as the root value and proceed with the function
        #In our case since current.left doesnt exist, we find 8.left = Node(7, current=8, 'red')

        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')

    def rebalance(self, node):
        #Case 1
        #Rule we are checking here is to make sure that the node's parent is not None
        if node.parent == None:
            return
        #Case 2
        if node.parent.color == 'black':
            return
        #Case 3
        

    def search(self, find_val):
        return False

