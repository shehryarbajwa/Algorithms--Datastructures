### The number of inversions in a disordered list is the number of pairs of elements that are inverted (out of order) in the list
### Inversions are where in pair the larger number is to the left

### [0,1] has 0 inversions
### [3,1,2,4] has 2 inversions 
### [7,5,3,1] has 6 inversions [7,5] [7,3] [7,1] [5,3] [5,1] [3,1]

### Counting inversions

def count_inversions(arr):
    start_index = 0
    end_index = len(arr) - 1
    output = inversions_count_func(arr, start_index, end_index)
    return output

def inversions_count_func(arr, start_index, end_index):

    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2
    

