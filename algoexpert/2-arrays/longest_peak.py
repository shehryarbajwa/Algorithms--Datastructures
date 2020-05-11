

#Time Complexity O(N)
# Space Complexity O(1)

def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        #left side
        #value at i - 1 is already smaller than peak value
        #Compare value after i - 2 with value after
        #If i - 2 is smaller than prior peak value, keep going left and keep checking for peaks

        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        
        #Right side
        #Value at i + 2 since i + 1 is already greater than peak value
        #Compare value after i + 2 with value at i + 1
        #If the value is smaller
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
        
        print(rightIdx)
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(currentPeakLength, longestPeakLength)
        i = rightIdx
    return longestPeakLength

print(longestPeak([3,4,8,10,6,5,-1,-3]))