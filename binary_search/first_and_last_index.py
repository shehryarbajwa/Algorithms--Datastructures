#Given a SORTED array that may have duplicate values, use binary search to find the first and last indexes of a given value
# For example if we have array = [0,1,2,2,3,3,3,4,5,6] and we are given 3 as value
# The answer will be [4,6] 4 being the first index, and 6 being the last index

def first_and_last_index(arr, number):

    first_index = find_start_index(arr, number, 0, len(arr) - 1)
    last_index = find_end_index(arr, number, 0, len(arr) - 1)
    return [first_index, last_index]

##Lets code out an example
#We have an array = [1,1,3,4,5] and target is 1
#start_index is 0
#end_index is len(arr) = 5 - 1 = 4
#def find_start_index(arr, 1, 0, 4)
#mid_index = 2
#arr[2] = 3 which is not number so we move on
#arr[2] < 1 is not true so we move on
#return find_start_index(arr, 1, start_index=0, end_index is changed to mid_index=2 - 1, end_index==1) by changing the end index, we
#recurse to left
#If arr[mid_index] > element, then we move to left. If arr[mid_index] < element, we move to the right
#We run the loop again to find to the left
#   find_start_index second time
#   start_index is 0
#   end_index is 1
#   mid_index = 1 /2 = 0 since we are not using float
#   start_index 0, end_index 1, mid_index is 0
#   arr[0] = 1
#   current_start_position checks whether any more positions before this
#       current_start_position = find_start_index(arr, 1, 0, 0 - 1)
#       if start_index > end_index which is 0 > -1 we return -1
#       current_start_position is now -1
#   start_position = mid_index which is 0
#   we return 0 as the starting position
#   starting position will get computed as long as start_index < end_index
#   arr [1,2,3,4]
#   arr[1,2]
#   arr[1]
#   arr[1] end_index becomes -1
#   When will current_start_position not be -1
#   When the element we are searching for is at the beginning of our array
#   if current_start_position is not -1 is all the times we are iterating over the array to keep moving to the left
#   start_position is set one number to the left
#   then again a number to the left
#   until it hits the point where start_index > end_index at which point we have checked all our elements to the left
#   to find the starting point
#   This is when we return the value and conclude the current_start_position function
#   Till then it keeps iterating

#   Now we do the same thing for the right index 


def find_start_index(arr, number, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index) // 2
    
    if arr[mid_index] == number:
        current_start_pos = find_start_index(arr, number, start_index, mid_index - 1)
        
        if current_start_pos != -1:
            start_pos = current_start_pos
        else:
            start_pos = mid_index
        return start_pos

    elif arr[mid_index] < number:
        return find_start_index(arr, number, mid_index + 1, end_index)
    else:
        return find_start_index(arr, number, start_index, mid_index - 1)

def find_end_index(arr, number, start_index, end_index):
    # binary search solution to search for the last index of the array
    if start_index > end_index:
        return  -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_end_pos = find_end_index(arr, number, mid_index + 1, end_index)
        if current_end_pos != -1:
            end_pos = current_end_pos

        else:
            end_pos = mid_index
        return end_pos
    elif arr[mid_index] < number:
        return find_end_index(arr, number, mid_index + 1, end_index)
    else:
        return find_end_index(arr, number, start_index, mid_index - 1)

print(first_and_last_index([-1,-2,0,1,2,3,4,4,4,4], 4))