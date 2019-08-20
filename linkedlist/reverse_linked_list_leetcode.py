#Reverse a singly linked list

class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

    
    def reverse(self,head):
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev