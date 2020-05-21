class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#Time Complexity O(N)
#Space Complexity O(N) for using a hash table
def remove_dups(head):

    hash_map = {}
    currentNode = head
    p1prev, p1 = None, currentNode

    while p1 is not None:
        
        if p1.value in hash_map:
            p1prev.next = p1.next
            p1 = p1.next
            continue

        p1prev = p1
        hash_map[p1.value] = True
        p1 = p1.next
    
    return head

#Time Complexity O(N^2)
# Space Complexity O(1)

def remove_dups_without_hash_map(head):

    current = head

    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head


