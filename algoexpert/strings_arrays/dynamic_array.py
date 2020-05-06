
# Array has a constant time lookup because it is storing the current index in RAM.
# If a[0] is at a memory location 2000, then a[1] is guaranteed to be at location 2002
# Thus the current index is cached and recalled from RAM making the access time a constant time operation
# The resizing cannot be done by RAM since it cant be stored before so that is a linear time operation but if we double the capacity it is amortized constant time operation of O(1)
# Array with its current index is stored in RAM.
# Resizing is done in O(N) time

#Space Complexity O(N) since we store the array in memory
class Dyanmic_array:
    def __init__(self, initial_size=10):
        self.array = [None for _ in range(initial_size)]
        self.current_index = 0
        self.end_index = initial_size

    #Time Complexity O(1) Average amortized case
    #Time Complexity O(N) if we have to resize the array
    #We can resize based on a fixed size so we lets say double
    #That means at each iteration we will have more empty indices and thus can achieve this in constant time
    def append(self, value):

        if (self.current_index == self.end_index):
            self.resize_array(self.array)

        self.array[self.current_index] = value
        self.current_index += 1

    #This requires scooting over the rest of the elements.
    #If we have an array [0,2,3,4,5,6]
    #We are asked to put an element at index 1 of 9
    #New array becomes [0,9,2,3,4,5,6]
    #Thus based on our input, the output increased linearly.
    #The output takes longer and longer to shift the indices based on what input we provide. Worst case pre-pend to the array
    def insertion(self, index, value):

        previous_value = None
        for i in range(len(self.array)):
            if i == index:
                previous_value = self.array[i]
                self.array[i] = value
                self.array[i + 1] = previous_value
            old_index_value = self.array[i]
            self.array[i + 1] = old_index_value

    #Time Complexity O(1)
    #Index is stored in RAM
    #That position with its value is held in computer memory because of array's fixed size.
    #It doesnt depend on input
    def access(self, index):
        if index < 0 or index > self.current_index:
            raise IndexError("Index out of range")
        
        return self.array[index]

    #Array elements are stored adjacent to each other. So when we remove an element, 
    #We have to fill in the gap—"scooting over" all the elements that were after it:
    #Array [0,4,5,6]
    #Remove 5
    #Now we have get [0,4, ,6]
    #Thus now have to scoot over each element
    #[0,4,6]
    #Thus what the input is the output changes with constant time
    
    def resize_array(self, array):
        new_array = [None for _ in range(len(self.array) * 2)]
        for index, element in enumerate(self.array):
            new_array[index] = element
        self.array = new_array

    #Time Complexity O(N) since we have to traverse the entire array to find a value

    def search(self, value):

        for i in range(len(self.array)):
            if value == self.array[i]:
                return value
        return None
        




    






