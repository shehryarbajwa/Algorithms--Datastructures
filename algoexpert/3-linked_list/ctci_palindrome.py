class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#Time Complexity O(N)
#Space Complexity O(1)
#We are changing the next pointers for half of the nodes. This was all memory that had already been allocated, so we are not using any extra memory and therefore it is O(1)O(1).

def palindrome(head):

    first = head
    second = reverse(head)

    while first is not None:
        if first.value != second.value:
            return False
        first = first.next
        second = second.next
    return True
#1-2-2-1
#Fast will go till 2
#Slow will go till second 2
#After reversal
#1-2 1-2
#Slow will reverse 2-1 to 1-2
#Then we compare 1 to 1 then increment and check 2 == 2
#If they are we have a palindrome
def reverse_palindrome(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    slow = reverse(slow)
    fast = head

    #Now slow will hit None value first
    while slow is not None:
        if slow.value != fast.value:
            return False
        slow = slow.next
        fast = fast.next

    return True


def reverse(head):

    p1,p2 = None, head

    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    
    return p1

linked_list = LinkedList(1)
linked_list.next = LinkedList(2)
linked_list.next.next = LinkedList(3)
linked_list.next.next.next = LinkedList(4)
linked_list.next.next.next.next = LinkedList(5)
linked_list.next.next.next.next.next = LinkedList(6)
