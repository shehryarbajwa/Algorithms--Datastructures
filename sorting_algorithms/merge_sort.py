### MergeSort is a divide and conquer algorithm
### We focus first on the divide portion of the algorithm
### Then we find if the list only has one single element in the list can be considered
### sorted and we can return immediately

### Here we are using recursion to solve this problem
### Lets look at an example
### Example is [1,2,4,3]
### mid = len(4) // 2 = 2
### left = [1,2]
### right = [3.4]
### left = merge_sort([1,2])
###     merge_sort([1,2])
###     mid = 2 // 2 = 1
###     left = [1]
###     right = [2]
###     left = merge_sort([1])
###         merge_sort([1])
###             return [1]
###     back to merge_sort([1,2])
###     left = [1]
###     right = [2]
###     return merge([1], [2])
###     
###     We run merge([1],[2])
###     merged = []
###     left_index = 0
###     right_index = 0

###     while left_index < len(left)=1 and right_index < len(right):
###     if left[left_index] == 1 > right[right_index]=2
#       or if 1 > 2
#       merged.append(left[left_index]) so merged now has [1]
#       left_index += 1
#       left index now becomes 1
#       since left index is not less than len(left) we break the loop
#       merged += left[left_index:] means merged += left[1:] -> None
#       merged += right[right_index:] means merged += right[0:] -> 2
#       so now merged has both 1 and 2 merged = [1,2]
#       return merged
#       merge_sort([1],[2]) -> returns merged = [1,2]
#       left = [1,2]
#       right = merge_sort([4],[3])
#       merge_sort([4],[3])
#       mid = 1
#       left = [4]
#       right = [3]
#       return merge([4], [3])
#       while left_index < len(left) and right_index < len(right)
#       if left[0]=4 > right[0]=3
#       since this is true, we will merged.append(3)
#       right_index +=1
#       now merged will be [3,4]
#       we return merge[3,4] to merge sort([3],[4])
#       
#       

def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

print(merge_sort([1,2,4,3]))
print(merge_sort([1,2,3,5,7,4,6,9]))
