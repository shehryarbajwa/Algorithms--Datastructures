class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution(object):
    def has_cycle(self, head):
        slow = head
        fast = head

        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return slow == fast

ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ll

print(Solution.has_cycle(ll))