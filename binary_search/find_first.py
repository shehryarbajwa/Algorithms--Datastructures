def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)

#The binary search function is guaranteed to return an index for the element you're looking 
# for in an array, but what if the element appears more than once?

#   [1, 3, 5, 7, 7, 7, 8, 11, 12]

#Find the first occurence of 7
#However, if we go nby recursive binary search

arr = [1, 3, 5, 7, 7, 7, 8, 11, 12]
print(recursive_binary_search(7, arr))

#This returns 7 to be at index 4
#However, we want it to return 7 at index 3 since that is its first occurence

#Find first only works if they array is sorted
#
def first_index(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    #In the above example, source[index] == 4 == target
    while source[index] == target:
        if index == 0:
            return 0
        #source[4-1 =3] == target
        #source[3] == 7
        #since 7 is target, index becomes 3
        #while source[index] == target is true now
        #both if statements wont be run and we will return index
        if source[index - 1] == target:
            index -= 1
        else:
            return index

#Lets take another example
arr2 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 8 , 8 , 9 , 9 , 9 ]
print(recursive_binary_search(8, arr2))

#Here when we do first_index, we find 8 to be returned at index 9, although first occurence is 
# at index 7
#in first occurence, we use the index which is 9
#while source[9] == 8:
#if source[index 9 - 1 = 8] == 8:
#source[8] == 8
#index gets decremented by 1 again
#We continue the loop
#if source[index = 8 - 1 = 7] == 8 i.e index[7] is 8 == target = 8
#Then index becomes decremented by 1 again

print(first_index(8, arr2))
