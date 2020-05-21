class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def shift_linked_list(head, k):
    
    list_length = 1
    list_tail = head

    while list_tail.next is not None:
        list_tail = list_tail.next
        list_length += 1

    jump = abs(k) % list_length

    new_tail_position = list_length - jump if k > 0 else jump

    new_tail = head

    for i in range(1, new_tail_position):
        new_tail = new_tail.next
    
    newHead = new_tail.next
    new_tail.next = None
    list_tail.next = head
    return newHead
    

