class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_kth_node(head,k):
    counter = 1
    first = head
    second = head

    #k = 4
    #Remove 1 from linked list
    #   0   1   2   3   4
    #When we start, we start at S and counter = 0
    #Then S goes up by 1 and then counter goes up by 1
    #When we reach 4.next = Null, our counter is 5 which is when we break the loop
    #Since we are running counter < and equal to k which is 4
    #while 1<=4, second = 0.next=1, c=2
    #while 2<=4, second = 1.next=2, c=3
    #while 3<=4, second = 2.next=3, c=4
    #while 4<=4  second = 3.next=4  c=5>
    while counter <= k:
        second = second.next
        counter += 1

    if second is None:
        head.value = head.next.value
        head.next = head.next.next

    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next

