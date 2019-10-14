class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_right_child(self, node):
        self.right = node

    def set_left_child(self, node):
        self.left = node
    
    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def has_left_child(self):
        return self.left != None
        
    def has_right_child(self):
        return self.right != None
        
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
    
    def get_root(self):
        return self.root

Node0 = Node("Fruits")
Node1 = Node('Banana')
Node2 = Node('Orange')
Node3 = Node('Pomegrenate')

Node0.set_left_child(Node1)
Node0.set_right_child(Node2)



print(f"""
value: {Node0.value}
left: {Node0.left.value}
right: {Node0.right.value}
""")

print(f"has left child? {Node0.has_left_child()}")
print(f"has right child? {Node0.has_right_child()}")
print(f"has left child? {Node2.has_left_child()}")
