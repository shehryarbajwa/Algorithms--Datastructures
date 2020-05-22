import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_middle_node(head, value):
    p1prev = None
    p1 = head

    while p1.next is not None:
        if p1.value == value:

            if p1prev is None:
                return

            #remove p1.value
            p1prev.next = p1.next
            p1 = p1.next
            continue
        p1prev = p1
        p1 = p1.next
    
    return head

linked_list = LinkedList(1)
linked_list.next = LinkedList(2)
linked_list.next.next = LinkedList(3)
linked_list.next.next.next = LinkedList(4)
linked_list.next.next.next.next = LinkedList(5)
linked_list.next.next.next.next.next = LinkedList(6)
remove_middle_node(linked_list, 4)

class Test(unittest.TestCase):
    def test_case_1(self):
        linked_list = LinkedList(1)
        linked_list.next = LinkedList(2)
        linked_list.next.next = LinkedList(3)
        linked_list.next.next.next = LinkedList(4)
        linked_list.next.next.next.next = LinkedList(5)
        linked_list.next.next.next.next.next = LinkedList(6)
        remove_middle_node(linked_list, 4)

        self.assertEqual(linked_list.next.next.next.value, 5)



if __name__ == '__main__':
    unittest.main()