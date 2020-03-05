class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    
    def addChild(self, value):
        self.children.append(Node(value))
        return self
    
    def breadthFirstSearch(self, bfsarray):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            bfsarray.append(current.value)
            for child in current.children:
                queue.append(child)
        return bfsarray



