"""
Problem Statement
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

Example 1:

arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.
Example 2:

arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.
"""

def max_sum_subarray(arr):
    #This is the Kadone algorithm which specifies that the maximum value at the nth index is either the nth
    #element or the max of the subarrays preceeding it

    #Subarrays are of contigous indices meaning 0,1,2,3 and not 1,3,2
    max_sum = arr[0]
    #We create two variables, max_sum which is the global sum of the subarray
    current_sum = arr[0]
    #Current sum takes the maximum sum of the subarrays till a given index

    for num in arr[1:]:
        #We start our iteration from the second element all the way till the last
        #current sum calculates whether the nth index is the max or the value of the previous subarrays meaning the index at 0 and index at 1 and their sum

        current_sum = max(current_sum + num, num)
        #As we iterate over the current sum, we keep updating the max sum. Max sum is the larger of the current sum of subarrays or the max sum
        max_sum = max(current_sum, max_sum)
    return max_sum

array = [1,-3,-4,5]
print(max_sum_subarray(array))