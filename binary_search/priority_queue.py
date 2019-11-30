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
 #       /           \
     #3(1)          4(2)
 #   /   \           /   \
 #4(3)    5(4)     6(5)  7(6)
 #/         \

 #If we insert 3 at index 7, since that is the first element we will be inserting at index 7
 #If however, we insert 2 at index 7
 #Then we have to upheapify
 #Which means to go one step up and remove 4 as parent and 2 as child and swap their positions
 #Then we will have to upheapify again twice first with 3 then with 1

 #In such a case, insertion takes O(1) time
 #In case of heapify, it could take O(height) which will take O(logn)
 #Time complexity of insert is O(log n)

class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index 

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            #Get the parent index which is current_index - 1 and divisible by 2
            #Parent index is the one containing the parent element
            #We can then get the parent element
            #Then find the child element at the current index
            #If parent element is > child element
            #Then we swap the element at the parent index with the child element
            #and element at the child index becomes the parent element
            #child index becomes parent index
            #Why? Because we are moving up the tree
            #child index becomes 0 and loop breaks
            #Now we insert an element again
            #Child index will keep getting the parent index and keep moving up
            #It breaks each time we hit the root of our tree
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            # compare with right child
            if right_child is not None:
                min_element = min(right_child, min_element)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

