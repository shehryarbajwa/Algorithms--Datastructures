
"""
Problem Statement
You have been given an array of length = n. The array contains integers from 0 to n - 2. Each number in the array is present exactly once except for one number which is present twice. Find and return this duplicate number present in the array

Example:

arr = [0, 2, 3, 1, 4, 5, 3]
output = 3 (because 3 is present twice)
"""

#This problem is solved with the pigeonhole problem. If there are 10 pigeons and 9 holes, 2 pigeons are in one hole

def duplicate_number(arr):
    #We keep track of the current sum
    #The sum of all indices is n * (n-1 / 2)
    current_sum = 0
    expected_sum = 0
    
    for num in arr:
        #We check the sum of all the values in the array and calculate the sum
        current_sum += num
    
    for i in range(len(arr) - 1):
        #We calculate the sum of all the indices of the array
        expected_sum += i
    #When we subtract the sum of values in the array from the indices, we can find which pigeon or value is stored twice
    return current_sum - expected_sum