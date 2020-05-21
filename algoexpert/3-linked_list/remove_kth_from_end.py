class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_kth_node(head, k):
    current, p1 = head, head.next

    while current is not None and p1.value is not k:
        current = current.next
        p1 = p1.next
    
    current.next = p1.next

LL = LinkedList(1)
LL.next = LinkedList(2)
LL.next.next = LinkedList(3)
LL.next.next.next = LinkedList(4)

print(LL.value)
print(LL.next.value)
print(LL.next.next.value)
print(LL.next.next.next.value)

print(LL.value)
print(LL.next.value)
print(LL.next.next.value)


