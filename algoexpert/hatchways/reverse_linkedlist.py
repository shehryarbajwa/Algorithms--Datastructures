def reverseLinkedlist(head):
    #p3 is not declared here, since it wastes memory and p3 is dependent on p2 so it has to keep changing on each iteration
    p1,p2 = None, head

    #When p2 is None, p1 is the final last node in the linked list
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1
