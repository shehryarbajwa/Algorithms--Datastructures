# 

# Given an array arr and a target element target, find the last index of occurence of target in arr using recursion. If target is not present in arr, return -1.

# For example:
# For arr = [1, 2, 5, 5, 4] and target = 5, output = 3
# For arr = [1, 2, 5, 5, 4] and target = 7, output = -1


def last_index(arr, target):
    return last_index_arr(arr, target, len(arr) - 1)

def last_index_arr(arr, target, index):

    if index < 0:
        return -1

    if arr[index] == target:
        return index

    return last_index_arr(arr, target, index -1)

print(last_index([1,3,4,5,7,8,9,10], 5))


# So we are doing this in O(n) time since we iterate over the array with the provided index. If that is not the case, we recurse again till we return the index or -1

# For example we have the array = [1,3,4,5,6]
# Our target is 3 which is at position 1 in the index
# We will start with last_index providing it the array and the target which is 3
# It will call another function last_index_arr which will take an array, target, and an index value
#   last_index_arr([1,3,4,5,6], 3, 4):
#       since index > 0 we continue
#       since arr[4] is 6 which is != 3 we continue
#       last_index_arr(arr, 3, 3):
#           since index > 0, we continue
#           arr[3] is 5 which is != 3, we continue
#           last_index_arr(arr, 3,2):
#               since index > 0 we continue
#               arr[2] is 4 so we continue
#                   last_index_arr(arr, 3,1):
#                       since index is > 0, we continue
#                       since arr[1] is 3 we return this value and exit the function
#                   since all previous functions are returning this function's final output and we are not storing it will keep returning and exit going all the way to the first function