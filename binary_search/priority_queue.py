# A priority queue is a a priority queue is similar to a regular queue, except that each element in the queue has a priority associated with it. 
# A regular queue is a FIFO data structure, meaning that the first element to be added to the queue is also the first to be removed.
# With a priority queue, this order of removal is instead based on the priority. 
# Depending on how we choose to set up the priority queue, we either remove the element with the most priority, 
# or an element of the least priority.
# For the sake of discussion, let's focus on removing the element of least priority for now.

#Other than a complete binary search, other data structures dont allow insertion and removal
# in any thing less than O(n) time

#We are creating a heap via an array data structure
#Insertion is quite simple
#We will always insert at the next index
#Once we have inserted an element, we will increment the value of next_index
#We also have to maintain the heap order property
#

#Min heap
            #1(0)
        /           \
     #3(1)          4(2)
    /   \           /   \
 #4(3)    5(4)     6(5)  7(6)
 /         \

 #If we insert 3 at index 7, since that is the first element we will be inserting at index 7
 #If however, we insert 2 at index 7
 #Then we have to upheapify
 #Which means to go one step up and remove 4 as parent and 2 as child and swap their positions
 #Then we will have to upheapify again twice first with 3 then with 1

 #In such a case, insertion takes O(1) time
 #In case of heapify, it could take O(height) which will take O(logn)
 #Time complexity of insert is O(log n)

class Heap:
    def __init__(self, intial_size):
        self.cbt = [None for _ in range(intial_size)]
        self.next_index = 0

    def insert(self, data):
        #Insert a new element at the next index
        self.cbt[self.next_index] = data

        #Up heapify checks whether the parent is < child
        #If it is swap, else continue
        self.up_heapify()

        #Increment the next index by 1
        self.next_index += 1

        #If next_index goes out of array bounds, we need to double the array
        #temp stores the current array
        #self.cbt becomes for 2 * len(self.cbt)
        #We double the array
         
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]
            
            #for index in range(self.next_index)
            #This allows us to look at the range index
            #Copy elements from the old array to the new array

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    
    def remove(self):
        pass

    def up_heapify(self):
        #child_index refers to the next_index
        child_index = self.next_index

        #while child_index is greater than equal to 1
        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

        

