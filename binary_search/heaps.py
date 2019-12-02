# Heaps are elements arranged in increasing or decreasing order
# Max is where the parent must have a value greater than the child
# Min is where the parent must have a value less than the child

# Input data: 4, 10, 3, 5, 1
         # 10(0)
#        /  \
     # 5(1)  3(2)
#    /   \
 # 4(3)    1(4)

# The above is a max heap where parent 10 is greater than its children i.e 5 and 3
# 4 and 1 are greater than 5

# Min heap
        # 2(0)
#        /  \
     # 3(1)  4(2)
#    /   \
 # 4(3)    5(4)

# Above is a min heap

# Since heaps are not binary trees, the peek is the parent root i.e 2 and 10 in min max
# A heap is complete when all levels except the last one are completely full
# In our examples above both 3 and 4 and 5 and 3 are full
# If the level isnt totally full, we add elements from the left to right

# The Big(O) notation for search in a min max heap tree is O(n)
# For example we will take the search of 1 in our max heap
# Worst case, we will have to traverse left and right of 10
# That is 2 steps
# Then we traverse left and right of 5 that is 2 steps until we hit 1
# In the worst case getting to 1 will take 5 steps. However, it can be done in 4
# O(n) 4/5 n is still 0.8 n which is O(n) to be approximate
# However, in the best case, we can also have it to be O(n/2). If we know the target is 6
# Then we start at 10, we traverse down
# We have 5 and 3
# We know 6 > 5 and 3 so we dont need to check the roots since 5 and 3's roots are smaller than 5 and 3
# Therefore we can do it in half the steps i,e O(n/2) which is still O(n) when approximated

# A priority queue is used to denote the severity of patient's illness and who comes in and gets checked first 

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
       #Up heapify goes from bottom to top
        print("inside heapify")
        child_index = self.next_index
      
       #child index is the last index of the array
       #while child_index >=1
       #parent_index becomes child index - 1 // 2
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

    def _down_heapify(self):
       #In down heapify we start from the root and traverse to the bottom
       #Parent index of 0 denotes the root index
        parent_index = 0

      #While parent index < self.next_index i.e 0 < 11, we continue the loop
      #left child index is 2 * 0 + 1 = 1
      #right child index is 2 * 0 + 2 = 2
        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
      #parent becomes self.cbt[0] the root
      #left child we keep None and rightChild to be None
      #because we need to know if the size of the cbt is more than 0
      #min element at initial value is parent
      #We set up parent to be self.cbt[0]
      #if left child index is < self.next_index
      #then left child is self.cbt[left_child_index]
      #same thing for right child index
      #if left child is not None
      #we find the minimum element from the parent aswell as the left child
      #we do the same for the right child
      #If we 
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
      #if min element is left chiild i.e parent is smaller than left child
      #We swap the values and make parent = left_child_index
      #Since parent becomes min_element we can now return the while loop
      #Similarly if the min element is the right child i.e parent is smaller than right child
      #We swap the values and make parent = right_child_index
      #Since parent becomes min element we can now return the while loop
            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

   #Minimum in a min heap will be the root element, we can then return the element at the root
   #get minimum()
    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

heap = Heap(10)
heap.insert(5)
heap.insert(4)
print(heap.cbt)
print(heap.remove())
print(heap.cbt)