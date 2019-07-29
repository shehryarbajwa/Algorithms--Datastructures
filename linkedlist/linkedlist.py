"""
Linked List practice
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = None

def traverse_list():
    current_node = head

    while(current_node is not None):
        print(current_node.value)
        current_node = current_node.next

traverse_list()

def create_linked_list(input_list):

        head = None
        tail = None

        for value in input_list:
                if head is None:
                        head = Node(value)
                        tail = head
                        # print(head.value)
                else:
                        tail.next = Node(value)
                        tail = tail.next
                        print(tail.value)
        return head

create_linked_list([9,3,4,5])

