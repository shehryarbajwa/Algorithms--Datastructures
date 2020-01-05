#Two Number Sum

#Write a function that takes in a non-empty array of distinct integers and an integer
#representing a target sum. If any two numbers in the input array sum up to the target sum,
#the function should return them in an array. If no two numbers sum up to the target sum, the function
#should return an empty array. Assume that there will at most one pair of numbers summing up to the target sum.

#Sample input: [3,5,-4,8,11,1,-1,6]
#Target Sum = 10
#Sample output = [-1,11]

#Naive Approach two For Loops
def twoNumberSumNaive(array, targetSum):
    for number in range(len(array) - 1):
        firstNumber = number
        for j in range(len(array)):
            secondNumber = j

            if firstNumber + secondNumber == targetSum:
                return [firstNumber, secondNumber]
    return []

#Space-time complexity
#O(n^2) Time
#O(1) Space

#Hash table approach
#Calculate X + Y = targetSum
#Iterate over the array, calculate Y = TargetSum - X, Check via constant operation whether Y exists in hash table

def twoNumberSum(array, targetSum):
    nums = {}
    for number in array:
        if targetSum - number in nums:
            return [targetSum - number, number]
        else:
            nums[number] = True
    return []

#Space-time complexity
#O(n) Time
#O(n) Space since we are storing the number in nums dictionary

print(twoNumberSum([1,2,3,4,5], 22))
