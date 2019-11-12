class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_head = self.head
        output_string = ""
        while current_head:
            output_string += str(current_head.value) + " -> "
            current_head = current_head.next
        return output_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def convert_to_list(self):
        output = []
        node = self.head

        while node:
            output.append(node.value)
            node = node.next
        return output

def union(linkedlist_1: LinkedList, linkedlist_2:LinkedList):

    list_1 = linkedlist_1
    list_2 = linkedlist_2

    list_all = list(set(list_1 + list_2))

    linked_list = LinkedList()
    for i in list_all:
        linkedlist.append(i)

    return linked_list