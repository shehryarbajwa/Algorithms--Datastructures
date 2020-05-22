class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#Time Complexity O(N)
#Space Complexity O(1) since we are only creating 4 dummy nodes. For the remaining nodes, we are just changing their pointers
def partition(head, pivot):

    p1prev = p1 = LinkedList(0)
    p2prev = p2 = LinkedList(0)

    while head:

        if head.value < pivot:
            p1prev.next = head
            p1 = p1.next

        else:
            p2.next = head
            p2 = p2.next
        
        head = head.next
    
    p2.next = None
    p1.next = p2prev.next

    return p1prev.next









