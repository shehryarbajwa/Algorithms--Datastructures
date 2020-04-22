
class Node(object):
    def __init__(self, data=None):

        self.data = data
        self.next = None

class linked_list:
    def __init__(self, data):
        self.head = Node(data)

    #O(1) time complexity
    def insert(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

    #O(N) time O(N) space
    def display(self):
        elements = []
        current_node = self.head
        elements.append(current_node.data)
        while current_node.next is not None:
            elements.append(current_node.next.data)
            current_node = current_node.next
        return elements

    #O(N) time O(1) space
    def search(self, data):
        current_node = self.head
        
        while current_node is not None:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        if current_node is None:
            return False

    #O(N) time O(1) space
    def delete(self, data):
        current_node = self.head
        prev_node = None

        while current_node is not None:
            if current_node.data == data:
                break
            else:
                prev_node = current_node
                current_node = current_node.next

        if current_node is None:
            raise ValueError("Data not in list")
        

        #   If removing the first node from the linked list
        #   1 -> 2
        #   Delete 2
        #   We can see that when we have to 2 delete 2, we have to make 1's next pointer point to Null

        # 1 -> 2 -> 3 -> 4
        # Remove 2
        # 1's next to 3


        if prev_node is None:
            self.head = current_node.next
        else:
            prev_node.next = current_node.next

        

    


            

my_list = linked_list(1)
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(5)
my_list.insert(7)
my_list.insert(9)
my_list.insert(11)
my_list.delete(11)

print(my_list.display())
print(my_list.search(3))
print(my_list.search(9))
print(my_list.search(91))
    

    




    

    
    


        

    