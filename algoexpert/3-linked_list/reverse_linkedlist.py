#Time Complexity O(N) for iterating over each node
#Space Complexity O(3) i.e O(1) for storing 3 pointers 
class Node(object):
    def __init__(self, data):

        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    #O(1) time complexity
    def insert(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    #Time Complexity O(N)
    #Space Complexity O(1)
    def reverseLinkedlist(self, head):
        p1,p2 = None,head

        while p2 is not None:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

        return p1

    #Time Complexity O(N)
    #Space Complexity O(N)
    def reverse_list_recursive(self, node):
        if node is None:
            return
        if node.next is None:
            return node.data
        
        head = self.reverse_list_recursive(node.next)
        node.next.next = node
        node.next = None
        return head

    def print_linked_list(self):
        current = self.head
        empty_list = []
        while current is not None:
            empty_list.append(current.data)
            current = current.next
        return empty_list

    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

ll = LinkedList(node1)
ll.insert(node2)
ll.insert(node3)

print(ll.print_linked_list())