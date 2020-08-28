
def distinct_pairs(array, target):
    array.sort()
    left = 0
    right = len(array) - 1
    count = 0

    while left < right:
        if array[left] + array[right] == target:
            count += 1
            while left < right - 1 and array[left] == array[left + 1]:
                left += 1
            left += 1

            while right > left and array[right] == array[right - 1]:
                right -= 1
            right -= 1

        elif array[left] + array[right] > target:
            right -= 1

        else:
            left += 1
    return count

print(21 // 10)

print(distinct_pairs([1,3,46, 1, 3, 9],47))
