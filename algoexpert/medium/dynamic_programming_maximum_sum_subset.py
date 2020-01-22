#Dynamic programming question

#Formula for calculating max sum of an array
#Maxsums[i] = Max( maxSums[i-1], maxSums[i-2] + originalArray[i])

#Two base cases
#First element in new array is first element of original array
#Second element in new array is bigger of first or second element of original array

#Time complexity O(N), comparisons in constant time
#Space complexity O(N), building a new array of length N

# Can we do better? No since we have to traverse the entire array.
# Space complexity, 

def maxSubsetSumNoAdjacent(array):

    #Edge cases

    #Assuming positive integers

    if len(array) == 0:
        return False

    elif len(array) == 1:
        return array[0]

    #Copy array
    maxSums = array[:]
    #Get the second number of maxSums to be max of first and second number
    maxSums[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])

    #Return the final value
    return maxSums[-1]

#O(N) time complexity
#O(1) Space complexity

def maxSubsetSumNoAdjacentSpace(array):

    if len(array) == 0:
        return False
    elif len(array) == 1:
        return array[0]
    
    second = array[0]
    immediate = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(immediate, second + array[i])
        second = immediate
        immediate = current

    return immediate

    



