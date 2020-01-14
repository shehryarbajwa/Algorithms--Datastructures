
# In place sorting is array.sort() This saves us memory and space
# Storing the array in a new DS like new_array = array.sort() takes more space O(N)
# By using infinites, we make sure that in the first iteration, our smallest difference gets updated
# If we keep it to smallest_difference=0 < current_difference:
# Then in second iteration, smallestDiff will be 1
# However in third iteration, smallestDiff will become 2 when currentDiff is 4-2
# So we skip 1, when it was the smallest difference
# Therefore using infinity works because it sets our smallest difference right in the first attempt
# If we do smallest difference > current_difference, we again wont be able to solve it, since 0 will never be bigger than 

# Time Complexity is O(Nlogn + MlogM) logN for sorting the algorithms and N for looping through them
# Space Complexity is O(1) since we are doing the sorting in place

def smallest_difference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idx_left = 0
    idx_right = 0
    smallest_difference = float('inf')
    current_difference = float('inf')

    while idx_left < len(arrayOne) and idx_right < len(arrayTwo):
        firstNum = arrayOne[idx_left]
        secondNum = arrayTwo[idx_right]

        if firstNum < secondNum:
            current_difference = secondNum - firstNum
            idx_left += 1

        elif firstNum > secondNum:
            current_difference = firstNum - secondNum
            idx_right += 1

        else:
            return [firstNum, secondNum]

        if smallest_difference > current_difference:
            smallest_difference = current_difference
            smallest_pair = [firstNum, secondNum]

    return smallest_pair


print(smallest_difference([1, 2, 1], [3, 4]))
