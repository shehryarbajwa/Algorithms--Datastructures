# Time complexity of this graph is O(v + e)
# We have v vertices and e edges
# The for loop runs O(e) times. 
# O(v) is for adding the vertices since there are V vertices and we traverse all V vertices
# O(e) refers to the number of times the for loop iterates over the children
# the children are denoted by the number of edges each vertice has

# You are given a Node class that has a name and an array of optional children Nodes. When put together, Nodes form a simple tree like structure. 
# However, it is not a binary tree. Implement a DFS which takes in an empty array, traverses the tree using DEPTH First search, 
# Stores all the Node's names in the input array and returns it.



# Space complexity is O(V)
# O(V) because for removing the first function from the call stack, we need to wait for the function executing at the leaf
# Since func executing at leaf at most will be n something, thus our space time is O(V).
# We store V different Nodes in the array we store the array we are given
# This is for appending to the array

class Node:
    def __init__(self,name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

n1 = Node('A')
n1.addChild('B')
n1.addChild('C')
n1.children[0].addChild('D')
n1.children[0].addChild('E')
n1.children[1].addChild('F')
n1.children[1].addChild('G')

print(n1.depthFirstSearch([]))
    