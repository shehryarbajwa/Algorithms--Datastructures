class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Time Complexity O(1)
    #Space Complexity O(1)
    def setHead(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = Node(value)
            return
        self.insertBefore(self.head)

    #Time Complexity O(1)
    #Space Complexity O(1)
    def setTail(self, value):
        if self.tail is None:
            self.setHead(value)
            return
        self.insertAfter(self.tail)

    #Time Complexity O(1)
    #Space Complexity O(1)
    def insertBefore(self, node, nodeToInsert):
        if self.head is None and self.tail is None:
            return

        self.remove(nodeToInsert)

        nodeToInsert.next = node
        nodeToInsert.prev = node.prev

        if node is self.head:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    #Time Complexity O(1) - We know the node so just need to change pointers
    #Space Complexity O(1)
    def insertAfter(self, node, nodeToInsert):
        if self.head is None and self.tail is None:
            return

        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node

        if node is self.tail:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    #Time Complexity O(P)
    #Space Complexity O(1)
    def insertAtPosition(self,position, nodeToInsert):

        if position == 1:
            self.setHead(nodeToInsert)

        count = 1
        prev = None
        currentNode = self.head

        while currentNode is not None and count != position:
            currentNode = currentNode.next
            count += 1

        if currentNode is not None:
            self.insertBefore(currentNode, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

        



    #Time Complexity O(N)
    #Space Complexity O(1)
    def search(self, value):
        currentNode = self.head
        found = False

        while currentNode is not None and found is False:

            if currentNode.value == value:
                found = True
            else:
                currentNode = currentNode.next

        if currentNode is None:
            raise ValueError('Value not found')
        return currentNode

    #Time Complexity O(1) - We know the node to remove
    #Space Complexity O(1)
    def remove(self, node):
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        remove_bindings(node)

    def remove_bindings(self, node):
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        node.next = None
        node.prev = None

    #Time Complexity O(N) - We have to traverse each node to find whether this is the one to remove
    def remove_node_with_value(self, value):
        currentNode = self.head

        while currentNode is not None:
            nodeToRemove = currentNode.value
            currentNode = currentNode.next
            if nodeToRemove == value:
                self.remove(nodeToRemove)

    

        








        

    
