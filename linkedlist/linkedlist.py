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
            print('The value of the head node is : ' + f'{head.value}')
        else:
            tail.next = Node(value)
            tail = tail.next
    print('The value of the tail node is : ' + f'{tail.value}')
    return


(create_linked_list([1,3,4,5,2,1,3,4,3,4,5,6,7,9,11,12,13,3,44,56,12,3,4,5,2,1,3,4,3,4,5,6,7,9,11,12,13,3,44,56, 13, 14, 12, 181,199999929193228939823892389]))

class singly_linked_list:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            print('The value of head is : ' + f'{self.head.value}')
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
            print('The value of node is : ' + f'{node.value}')
        
        node.next = Node(value)
        print('The value of tail is : ' + f'{node.next.value}')
        return 

linked_list = singly_linked_list()
linked_list.append(1)
linked_list.append(2)
# linked_list.append(3)
# linked_list.append(4)
# linked_list.append(6)

node = linked_list.head
while node:
    print(node.value)
    node = node.next

