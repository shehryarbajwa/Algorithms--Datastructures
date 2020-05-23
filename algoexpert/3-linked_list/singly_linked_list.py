class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    #Time Complexity O(1)
    #Space Complexity O(N)
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #Time Complexity O(1)
    def delete_at_beginning(self):

        prev = self.head
        self.head = self.head.next
        prev.next = None

    #Time Complexity O(N)

    def append(self, data):
        current = self.head

        while current.next is not None:
            current = current.next
        
        current.next = Node(data)

    #Time Complexity O(N)
    #Space Complexity O(1)
    def search(self, data):
        current = self.head

        found = False
        while current and found is False:
            if current.value == data:
                found = True
            else:
                current = current.next
        if current is None:
            raise ValueError('Could not find data')
        return current


    #Time Complexity O(N)
    def delete(self, data):
        current = self.head
        previous = None
        found = False

        while current and found is False:
            if current.value == data:
                found = True
            else:
                previous = current
                current = current.next

        if current is None:
            raise ValueError('Could not find data')

        previous.next = current.next

    
    