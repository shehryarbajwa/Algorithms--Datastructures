import unittest
import program


#Time Complexity O(V + E)
#Traverse all nodes at one point

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, value):
        self.children.append(Node(value))
        return self

    
    #1-Add the vertex to start the breadthFirstSearch to the empty queue
    #2-Mark that vertex visited
    #3-Extract a vertex from the queue and add its neighbors to the queue if that isnt marked visited
    #4-Repeat step 3 until the queue is empty

    def breadthFirstSearch(self, bfsarray):
        #Add the first vertex. Self refers to the first value of the graph/tree
        queue = [self]
        while len(queue) > 0:
            #Get the first element of the tree
            current = queue.pop(0)
            #Add it to viisted array
            bfsarray.append(current.value)
            #Add its children to the queue
            for child in current.children:
                queue.append(child)
            #keep running the loop till the queue becomes emtpy
        return bfsarray

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test1 = Node('A')
        test1.addChild('B').addChild('C')
        
        self.assertEqual(test1.breadthFirstSearch([1]))
