
#Time Complexity O(N)
#Space Complexity O(1)

def subarray_sort(array):

    minimum_out_of_order = float('inf')
    maximum_out_of_order = float('-inf')

    for i in range(len(array)):
        num = array[i]

        if is_out_of_order(i, num, array):
            minimum_out_of_order = min(minimum_out_of_order, num)
            maximum_out_of_order = max(maximum_out_of_order, num)

    #Edge case - Input array is already sorted - return [-1,-1]
    if minimum_out_of_order == float('inf'):
        return [-1,-1]
    
    #Find the starting and ending indices of min,max in original array
    subarrayleftIndex = 0
    while minimum_out_of_order >= array[subarrayleftIndex]:
        subarrayleftIndex += 1
    subarrayrightIndex = len(array) - 1
    while maximum_out_of_order <= array[subarrayrightIndex]:
        subarrayrightIndex -= 1
    return [subarrayleftIndex, subarrayrightIndex]
    

def is_out_of_order(i, num, array):
    #First num in array - nothing to left
    if i == 0:
        return num > array[i + 1]
    #Last num in array - nothing to the right
    if i == len(array) - 1:
        return num < array[i - 1]

    #Either the number is greater than the next number
    #Or the number is smaller than the previous number
    return num > array[i + 1] or num < array[i - 1]


    
