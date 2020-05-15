
#Brute Force Solution
#Time Complexity O(N log N)
#Space Complexity O(N)
def longest_range(array):
    temp_result = []
    result = []

    array.sort()

    i = 1

    while i < len(array):

        if i == 1:
            temp_result.append(array[i - 1])

        if array[i] - array[i - 1] == 1:
            temp_result.append(array[i])

        elif array[i] - array[i - 1] > 1:
            break
        i += 1

    result.append(temp_result[0])
    result.append(temp_result[-1])


    return result

#Efficient Solution
#Time Complexity O(N)
#Space Complexity O(N)


def efficient_longest_range(array):
    bestRange = []
    nums = {}
    longestLength = 0

    for num in array:
        nums[num] = True

    for num in nums:
        if nums[num] == False:
            continue
        nums[num] = False
        left = num - 1
        right = num + 1
        currrentLength = 1

        while left in nums:
            currrentLength += 1
            nums[left] = False
            left -= 1

        while right in nums:
            currrentLength += 1
            nums[right] = False
            right += 1

        if currrentLength > longestLength:
            longestLength = currrentLength
            bestRange = [left + 1, right - 1]

    return bestRange

print(efficient_longest_range([1,11,3,0,15,5,2,4,10,7,12,6]))
