class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, value):
        #In the case of a stack, self.push.append() pushes items at the top of the stack
        self.items.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            #In case of a stack self.items.pop() removes the item at the top of the stack
            return self.items.pop()

class Queue:
    def __init__(self):
        self.instorage=Stack()
        self.outstorage=Stack()
        
    def size(self):
         return self.outstorage.size() + self.instorage.size()
        
    def enqueue(self,item):
        self.instorage.push(item)
        
    #For example, we are given an input of 1,2,3. We push 1 then 2 then 3 to our enqueue list [1,2,3]
    #Then we take element out from enqueue by pop so 3 then 2 then 1 and append it to the outstorage stack like [3,2,1]
    def dequeue(self):
        #Check if self.outstorage.items is empty
        #Once we have pushed the item to the stack, we stop the loop
        #Since we are returning the pop value of the outstorage stack, when we finish the function, the outstorage is empty
        #It will add one element the popped element, then pop it again leaving the stack empty each time the function is run
        if not self.outstorage.items:
            #Iterate over the enqueue stack
            while self.instorage.items:
                #For each element in the enqueue stack, remove the element at the last index and append it to dequeue stack
                self.outstorage.push(self.instorage.pop())
        return self.outstorage.pop()
    

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.size())

print(q.dequeue())
print(q.dequeue())
print(q.size())