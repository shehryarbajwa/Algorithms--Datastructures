## BubbleSort

#   In the beginning we assume, the array is not sorted so we can traverse
#   While not sorted
#   While needs a condition to break out of the loop
#   While we iterate, we change to isSorted as a break condition
#   When we find that number at 0 is greater than 1, we swap and setIsSorted to False
#   This keeps happening. When the if statement is no longer true
#   We go back up and changeisSorted back to True again
#   We need to do isSorted = False so that we can run the algorithm on the function again a second time
#   This way, when we run it again in the while loop, we traverse again sort again
#   Then after x attempts, when it gets finally sorted, then we wont have the if conditional true and we can just break out of the loop

# Time Complexity is O(N) for best case where array is already sorted
# Average Case and Worst Case O(N^2) where we iterate over the list multiple times running the for loop. When its 2 its still O(n^2) or whether its 100
# Space Complexity O(1) because we are swappning on the original array and not using any new Data structure to hold values. Therefore we are not using memory for additional data structures. BubbleSort is in order



def bubbleSort(array):
    isSorted = False
    
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1):
            if array[i + 1] < array[i]:
                swap(i + 1, i , array)
                isSorted = False
    return array

def swap(i, j , array):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

    # array[i], array[j] = array[j], array[i]

print(bubbleSort([1,2,-1,4,11,19,6,4]))