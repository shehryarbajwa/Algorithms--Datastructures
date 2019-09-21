class Queue:

    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        #-1 means there are no elements in the queue and it is empty
        #-1 is just to denote that there are no elements. If we set it to 0, it can show that the element at 0 is the front_index
        #In case not to confuse things, we keep -1. It can be any number. It can be None
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        #If the queue exceeds the length of the array that we have built for a capacity of 10 elements, then we need to make a new array

        if self.queue_size == len(self.arr):
            _handle_queue_excess_capaity()
        
        #Enqueue means to add to the queue. A new person gets in line
        #We add the next person at the next index
        self.arr[self.next_index] = value
        self.queue_size += 1
        #The next index will be set to 0 initially and increment by 1. 1 % 10 is 1. 2 % 10 is 2 ... Once it reaches the end
        #We can check if there were elements that were taken out of the queue, then we can add the new element in that memory position
        #Otherwise we can create a new one
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            return None
        #Front returns the element at the front index
        return self.arr[self.front_index]

    def dequeue(self, value):
        #Dequeue means to remove the value at the front
        if self.is_empty():
            #If the queue is empty after removing all elements we return None and reset the pointers so if we add new elements it begins from position 0

            self.next_index = 0
            self.front_index = -1
            return None
        #Value means returning the value at the front index
        value = self.arr[self.front_index]

        #We keep incrementing the front index by 1 with the modulus. When we reach the end of the queue, i.e 10 % 10 is 0 
        #If we have removed all the first 9 elements, then the front index should reset to zero for the next element since there are none left
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value
    
    def _handle_queue_excess_capaity(self):
        #Copy the old array and create a new array twice its length
        old_arr = self.arr
        self.arr = (for _ in range(2 * len(old_arr)))

        index = 0
        #We copy elements in two phases. If we had Ali at the front, then me and then jeff, in our new array we want the same position
        #So we copy from the front_index till the end of the line so Ali till Jeff
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1
        
        #Once we have copied from Ali till Jeff, then we copy the elements i.e the new elements we have added or who entered the queue
        #After Jeff new guy is Ahmed, then Rana then Aamer
        #So now we copy from Ahmed at 0 to Aamer that is till the front.index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1
        
        #In the new array, Ali is at 0 now so we reset the index
        self.front_index = 0
        #And the next index to add is after Aamer which is the last value of the index
        self.next_index = index
