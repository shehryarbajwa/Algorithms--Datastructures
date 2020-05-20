import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)


    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node is self.tail:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node is self.head:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
        
        currentNode = self.head
        currentPosition = 1

        while currentNode is not None and currentPosition is not position:
            currentNode = currentNode.next
            currentPosition += 1
        
        if currentNode is not None:
            self.insertBefore(currentNode, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        currentNode = self.head

        while currentNode is not None:
            nodeToRemove = currentNode
            currentNode = currentNode.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
    
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeBindings(node)

    def removeBindings(self, node):
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        node.next = None
        node.prev = None

    def contains(self, value):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value == value:
                return True
            else:
                currentNode = currentNode.next
        return False

    def print_nodes(self):
        nodes = []
        currentNode = self.head
        while currentNode is not None:
            nodes.append(currentNode.value)
            currentNode = currentNode.next
        return nodes


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

ll = DoublyLinkedList()
ll.setHead(node1)
ll.insertAfter(node1,node2)
ll.insertAfter(node2,node3)
ll.setTail(node4)
print(ll.print_nodes())


class Tests(unittest.TestCase):
    def test_case_1(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        ll = DoublyLinkedList()
        ll.setHead(node1)
        ll.insertAfter(node1,node2)
        ll.insertAfter(node2,node3)
        ll.setTail(node4)
        self.assertEqual(ll.print_nodes(), [1,2,3,4])

    def test_case_2(self):
        node1 = Node(1)
        node2 = Node(8)
        node3 = Node(3)
        node4 = Node(4)
        ll = DoublyLinkedList()
        ll.setHead(node1)
        ll.insertAfter(node1,node2)
        ll.insertAfter(node2,node3)
        ll.setTail(node4)
        self.assertEqual(ll.print_nodes(), [1,8,3,4])



if __name__ == "__main__":
    unittest.main()