# The first thing that comes to mind is that there should a linear time solution since
# we have to traverse the entire array
# O(N^2) since remove has to traverse the entire array and find the element to remove
#  A linear scan time is necessary in order to find the item before it can be removed


def moveElementtoEnd(array, moveTo):
    i = 0
    j = len(array) - 1

    while i < j:
        #If the element at j is the one we have to moveTo, 
        # then we need to backtrack till we get to the element that is not the moveTo element
        
        while i < j and array[j] == moveTo:
            j -= 1
        
        #Here once we do the swap, only then we increment i by 1
        #If a number i.e 1 doesnt need to be movedToEnd we just incremenet i
        # I is our left Pointer so it has to move regardless of being moved or not
        #When it has to be swapped, it will be swapped and then i will incremenet
        if array[i] == moveTo:
            array[i], array[j] = array[j], array[i]
        i += 1
    
    return array

print(moveElementtoEnd([1,1,2,3], 1))