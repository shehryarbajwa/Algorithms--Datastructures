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
        # print(current_node.value)
        current_node = current_node.next

traverse_list()

def create_linked_list(input_list):

    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
            print('The value of the head is : ' + f'{head.value}')
        else:
            tail.next = Node(value)
            tail = tail.next
    print('The value of the tail is : ' + f'{tail.value}')
    return


print(create_linked_list([1,3,4,5]))

class singly_linked_list:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return 

