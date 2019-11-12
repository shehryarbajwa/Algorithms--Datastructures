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

    list_1 = linkedlist_1.convert_to_list()
    list_2 = linkedlist_2.convert_to_list()

    list_all = list(set(list_1 + list_2))

    linked_list = LinkedList()
    for i in list_all:
        linked_list.append(i)

    return linked_list

def intersection(linkedlist_1: LinkedList, linkedlist_2:LinkedList):
    set_1 = set(linkedlist_1.convert_to_list())
    set_2 = set(linkedlist_2.convert_to_list())

    intersection_set = []
    for element in set_1:
        if element in set_2:
            intersection_set.append(element)

    linked_list = LinkedList()

    for i in intersection_set:
        linked_list.append(i)

    return linked_list

##Test cases
#Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

array_1 = [1,2,3,4,5]
array_2 = [5,6,7,8,9]

for i in array_1:
    linked_list_1.append(i)

for i in array_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

##Test Case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

array_3 = [1,3,5,7,9]
array_4 = [9,11,13,15,17,19]

for i in array_3:
    linked_list_3.append(i)

for i in array_4:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

##Test Case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

array_5 = [0,1,2,3,4,5,6]
array_6 = [7,8,9,10,11,12,13]

for i in array_5:
    linked_list_5.append(i)

for i in array_6:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))
