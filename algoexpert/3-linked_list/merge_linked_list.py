class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
#Time Complexity O(N + M)
#Space Complexity O(1)

def merge_linked_list(headOne, headTwo):
    p1 = headOne
    prev = None
    p2 = headTwo

    while p1 is not None and p2 is not None:
        #No need for mutation
        if p1.value < p2.value:
            prev = p1
            p1 = p1.next

        else:
            #Because prev is pointing to p1 which is bigger than p2
            if prev is not None:
                prev.next = p2
            #Then update prev to be the smaller value as prev notifies one before current linked list
            prev = p2
            p2 = p2.next
            prev.next = p1
    if p1 is None:
        prev.next = p2
    
    return headOne if headOne.value < headTwo.value else headTwo
            