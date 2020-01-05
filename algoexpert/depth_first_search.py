#Time complexity of this graph is O(v + e)
# We have v vertices and e edges
# The for loop runs O(e) times. 
# O(v) is for adding the vertices since there are V vertices and we traverse all V vertices
# O(e) refers to the number of times the for loop iterates over the children
# the children are denoted by the number of edges each vertice has


# Space complexity is O(V)
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

    