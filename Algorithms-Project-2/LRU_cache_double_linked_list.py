class Node:

    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dictionary = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.previous = self.head

    #head of LinkedList -> tail of linkedList
    #head of LinkedList <- tail of linkedlist


    #In a get request, we will remove the element first if we find it
    #Once it is removed, we will then add it so that it can move to the front of the cache

    def get(self, key):
        if key in self.dictionary:
            n = self.dictionary[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def set(self, key, value):
        if key in self.dictionary:
            self._remove(self.dictionary[value])
        n = Node(key, value)
        self._add(n)
        self.dictionary[key] = n

        if len(self.dictionary) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dictionary[n.key]
    
    #In remove, we have to change the pointers of the next and previous node
    #We are given the current node
    #First we find the previous node
    #Then we find the next node
    #Then we set previous node's next pointer to next node
    #Then we set next node's previous pointer to the previous node
    def _remove(self, node):
        previous = node.previous
        _next = node.next
        previous.next = _next
        _next.previous = previous


    #In add, we have to change the pointers of the tail and the head as the node comes in between the head and the tail
    #We find the head tail first
    #previous is tail's previous pointer which points to head
    #previous's next pointer points to the new node that was created
    #tail's previous previously pointed to the head node but now to the new node
    #new node's previous pointer now points to the previous node which is the head
    #new node's next pointer points to the tail of the linked list

    ##### Add brings an element to the front of the cache
    def _add(self, node):
        previous = self.tail.previous
        previous.next = node
        self.tail.previous = node
        node.previous = previous
        node.next = self.tail