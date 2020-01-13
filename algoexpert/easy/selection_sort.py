# Selection sort sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning

# Two given arrays:
# Subarray which is already sorted
# Remaining subarray which is unsorted

# Time Complexity Best, Average and Worst is O(N^2)
# Space Complexity is O(1)

# What are we doing? We create two subarrays in our original array and we traverse through them
# First we set up the minimum value as the first iterated i value
# If the first value is greater than the second for loop's first value, we can call the second value the minimum value
# We then check each time if minimum value is greater than any other value in the array. If it is we set that as our new minimum value
# This way, we find the minimum value and then swap the first value with the minimum value and now we have a subarray of sorted values

# We do the same for each iteration of outer for loop until we have a sorted array

# No matter what we still have to do two for loops

A = [0,0,0,-1,-2,-3,91,2,3,81,7,71, 8, 90, 9, 32,33,34,31,29,28,27] 

def selectionSort(array):

    for i in range(len(array)):

        minimum_index = i

        for j in range(i+1, len(array)):
            if array[minimum_index] > array[j]:
                minimum_index = j

        swap(i, minimum_index , array)
    return array

def swap(i, j , array):
    array[i], array[j] = array[j], array[i]

print(selectionSort(A))