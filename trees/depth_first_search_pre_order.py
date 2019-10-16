# There are a total of 10 functions for the Node class that we rely on
# 1-Initializing the Node class with value, left, right
# 2-Set value of the Node 
# 3-Get value of the Node
# 4-Set the left child of the Node by passing in a node
# 5-Set the right child of the Node by passing in a node
# 6-Get the left child of the Node - the node object
# 7-Get the right child of the Node - the node object
# 8-Check if left child exists - return True/False
# 9-Check if right child exists - return True/False

# For the Tree Class, we need to set up the initial root value
# 1-Set up the root value
# 2-Get the root value

# For the state Class
# 1-Node's value
# 2-Check if left node is visited
# 3-Check if right node is visited
# 4-Get True/False if left node is visited
# 5-Get True/False if right node is visited
# 6-Set the value to True if left node is visited
# 7-Set the value to True if right node is visited

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_right_child(self, Node):
        self.right = Node

    def set_left_child(self, Node):
        self.left = Node
    
    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def has_left_child(self):
        return self.left != None
        
    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"
        
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
    
    def get_root(self):
        return self.root


class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    

def pre_order(tree):
    visited_list = list()
    stack = Stack()

    #We fetch the node value from the root value of the Node
    node = tree.get_root()
    visited_list.append(node.get_value())
    #We create the state which contains the node and provide it the node
    state = State(node)
    #Then on the stack we push the state which is just the node and references to left and right child if they have been visited
    stack.push(state)

    count = 0

    while(node):
        print(f"""
        loop count: {count}
        current node: {node}
        stack:{stack}
        """)

        count += 1

        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            #Get the next node by getting the root's left child
            node = node.get_left_child()
            visited_list.append(node.get_value())
            #Next we set the state again with the Node value to be 'B'
            state = State(node)
            stack.push(state)
        
        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visited_list.append(node.get_value())
            state = State(node)
            stack.push(state)

        else:
            #Pop the value of D
            stack.pop()
            if not stack.is_empty():
                #State becomes the head value of the stack which now will be 'B'
                #Thus the node's value also becomes B
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    return visited_list

## Using recursion to solve the problem

def pre_order_tree(Tree):

    visit_order = list()
    root = Tree.get_root()

    def traverse(node):
        if node:
        #Visit the element
            visit_order.append(node.get_value())

            #Traverse left
            traverse(node.get_left_child())

            #Traverse right
            traverse(node.get_right_child())

    traverse(root)

    return visit_order


# In pre_order_tree we start with Apples, left child Banana, left child Dates, and Apple's right child Cherry

# The root is apple
# We use apple and run the traverse function
# In our visit_order list we append Apple
# Then we do recursion
# We then recurse
# At a time we first run the traverse(left_child function) and once it finishes run the traverse(right_child) function
# So we provide traverse with the left child which is Banana
# It runs the function and appends Banana to the list
# It then runs Dates function
# Meanwhile when dates finishes, Banana checks for a right child
# If it is none the function finishes
# All this keeps happening while Apple checks for the right node aswell





Node0 = Node("Apple")
Node1 = Node('Banana')
Node2 = Node('Orange')
Node3 = Node('Pomegrenate')

Node0.set_left_child(Node1)
Node0.set_right_child(Node2)
Node1.set_left_child(Node3)

print(f"""
value: {Node0.value}
left: {Node0.left.value}
right: {Node0.right.value}
""")

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


# (pre_order(tree))

print(pre_order_tree(tree))