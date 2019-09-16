class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elemenets = 0

    #Add an element to the top of the stack
    #The push at top means whatever we add on top would become the last element added and the only one accessible
    #Look at it as if you are adding a new cookie
    #The final cookie will be the one at the last index of the array

    def push(self , data):

        if self.next_index == len(self.arr):
            print("Out of space. Increasing stack capacity...")
            self._handle_stack_capacity()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elemenets += 1

    #If the size of the stack is full, we increase the stack capacity and assign the new stack the values
    #from the old array using the enumerate function. On the index value from old array we provide 
    #the element values

    def _handle_stack_capacity(self):
        old_arr = self.arr

        self.arr = [0 for _ in range(2 * len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

    def size(self):
        return self.num_elemenets

    def is_empty(self):
        if self.num_elemenets == 0:
            return True
        else:
            return False
    
    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elemenets -= 1
        return self.arr[self.next_index]

foo = Stack()
foo.push('Test')
foo.push('Hello')
foo.push('Nic')
foo.push('Nico')
foo.push('Nit')
foo.push('Ne')
foo.push('N')
foo.push('Noo')
foo.push('Nai')
foo.push('Nails')
foo.push('Dogtor')
print(foo.arr)
print(foo.num_elemenets)