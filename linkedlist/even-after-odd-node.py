
"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#So The solution is very intuitive. But it is not trivial to write a concise and bug-free code.

# A well-formed LinkedList need two pointers head and tail to support operations at both ends. 
# The variables odd and odd_tail are the head pointer and tail pointer of one LinkedList we call oddList; the variables even and even_tail are the head pointer and tail pointer of another LinkedList 
# we call evenList. The algorithm traverses the original LinkedList and put the odd nodes into the oddList and the even nodes into the evenList. 
# To traverse a LinkedList we need at least one pointer as an iterator for the current node. 
# But here the pointers odd and even not only serve as the tail pointers but also act as the iterators of the original list.




def even_after_odd(head):
    
    if head is None:
        return head
    #Set the even value and the odd value to be None initially and their tails aswell
    even = None
    odd = None
    even_tail = None
    odd_tail = None
    
    #While head is not true
    while head:
        #The next node will contain the pointer to the next node
        next_node = head.next
        
        #If the value of the head is divisible by 2, and there is no remainder left, we can say its even
        #If it is the first time we are seeing an even number, we will set even to be the head
        #We will also set the even's tail to be even at this stage
        if head.data % 2 == 0:
            if even is None:
                even = head
                even_tail = even
            else:
        #If the first even digit has already been initialized, then we will set the even_tail.next to be the head
        #Even tail is being brought forth from the previous loop
        #Even tail refers to the tail element of the even linked list. It will keep traversing till it reaches the end of the linked list
                even_tail.next = head
                even_tail = even_tail.next
        else:
        #We then do the same thing with the oddList and we keep updating the oddLinkedList
        #odd will be first odd number
        #odd tail will be the last element of the oddLinkedList
            if odd is None:
                odd = head
                odd_tail = odd
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next
        head.next = None
        head = next_node
    
    #This is where we merge the two lists together
    #If there was no odd number in our input array, then we can just return the even list
    #Once we have both the tails for odd_tail and even_tail, we will make the odd_tail's next element to be even
    #Remember even is the first even number in our linked list
    #Once we set this, the last element of the oddList will point to the first element of the evenList
    #Now we will start with even and end till even_tail and then finishing the entire loop
    if odd is None:
        return even
    odd_tail.next = even
    return odd

def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

linkedList = create_linked_list([2,4,6])
even = even_after_odd(linkedList)
print_linked_list(even)