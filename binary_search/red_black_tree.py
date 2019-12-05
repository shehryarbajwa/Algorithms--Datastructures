### Red black tree rules
### 1-All nodes have a color
### 2-All nodes have two children (use NULL nodes)
### 3-All null nodes are colored black
### 4-If a node is red, its children must be black
### 5-The root node must be black
### 6-Every path to its descendant NULL nodes must contain the same number of black nodes
### If we have a black aunt, we rotate
### If we have a red aunt, we color flip
### If we have a black aunt, we rotate the parent left if node inserted has a parent on the left side of its parent.
### If we have a black aunt, we rotate the parent right if node inserted has a parent on the right side of its parent.


class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_color = "R" if self.color == 'red' else "B"
        return '%d%s' % (self.value, print_color)

def grandparent(node):
    if node.parent == None:
        return None
    return node.parent.parent

def pibling(node):
    p = node.parent
    gp = grandparent(node)

    if gp == None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left

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
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):
        #Case 1
        #Rule we are checking here is to make sure that the node's parent is not None
        if node.parent == None:
            return
        #Case 2
        if node.parent.color == 'black':
            return
        #Case 3
        #The parent and its sibling of the newly inserted node are both red
        #In case the parent and the sibling of the newly inserted node
        #For example parent is 5
        #Newly inserted node is 3 which is black
        #Sibling of 3 is red
        #Now we have two reds
        #Parent and sibling so its not a red black tree since we cant have two consecutive reds
        #4-If a node is red, its children must be black
        #And then we will make sure that the grandparent is red
        #And swap the color of sibling and parent
        if pibling(node) and pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))

        #Case 4
        #The newly inserted node has a red parent but that parent has a black sibling
        #Inside refers to:

        gp = grandparent(node)
        if gp == None:
            return
        #The new node being a right child of its parent but the parent being a left child of its parent
        if gp.left and node == gp.left.right:
            self.rotate_left((node.parent))
        #The new node being a left child of its parent but the parent is a right child of its parent
            self.rotate_right((node.parent))

        #Case 5
        #Case 5 is for the outside when the new node inserted and its parent are on the same side of the grandparent
        #Newly inserted node has a red parent
        #Red parent has a black sibling

        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'

    
    def rotate_left(self, node):
        #Save off the parent of the sub-tree we're rotating
        p = node.parent
        #After node moves up, the right child will now be a left child
        node_moving_up = node.right
        node.right = node_moving_up.left
        #Node moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        #Now we need to connect to the sub-tree's parent
        #node may have been the root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up
        #In rotations, we just change the pointers of different nodes
        #And swap the values of the nodes
        #Rotation only happens when there is a red aunt or a black aunt
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p


    def search(self, find_val):
        return False

tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)

