# The first thing that comes to mind is that there should a linear time solution since
# we have to traverse the entire array
# O(N^2) since remove has to traverse the entire array and find the element to remove
#  A linear scan time is necessary in order to find the item before it can be removed


def moveElementtoEnd(array, moveTo):
    i = 0
    j = len(array) - 1

    while i < j:
        while array[j] == moveTo:
            j -= 1
        
        if array[i] == moveTo:
            array[i], array[j] = array[j], array[i]
        i += 1
    
    return array

print(moveElementtoEnd([1,1,2,3], 1))