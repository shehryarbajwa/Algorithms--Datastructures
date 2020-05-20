class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#Time Complexity O(N) - At most we traverse the entire total linked list length
#Space Complexity O(1)

#Our first node travelled through N nodes

def find_loop(head):

    hash_map = {}
    current = head

    while current is not None:
        if current.value in hash_map:
            break
        else:
            hash_map[current.value] = 1

        current = current.next
    
    return current.value


def find_loop_pointers(head):
    first = head.next
    second = head.next.next

    while first != second:
        first = first.next
        second = second.next.next

    first = head
    while first != second:
        first = first.next
        second = second.next
    return first
