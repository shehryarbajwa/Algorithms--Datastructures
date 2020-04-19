
class Node(object):
    def __init__(self, data=None):

        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = Node()

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

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        return elements

    def search(self, index):
        if index >= self.length():
            print("Error: 'Provided' index out of range")
            return None
        
        current_index = 0
        current_node = self.head
        print(current_node.data)

        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def delete(self, index):
        if index >= self.length():
            print("Error: Provided index out of range")
            return None
        current_index = 0
        current_node = self.head

        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

    


            

            
            



my_list = linked_list()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)

print(my_list.search(0))
print(my_list.display())

    

    




    

    
    


        

    