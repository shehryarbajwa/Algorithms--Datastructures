def same_bst(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if arrayOne[0] != arrayTwo[0]:
        return False
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    leftOne = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightOne = getBiggerOrEqual(arrayOne)
    rightTwo = getBiggerOrEqual(arrayTwo)

    return same_bst(leftOne, leftTwo) and same_bst(rightOne, rightTwo)

def getSmaller(array):
    smallest = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smallest.append(array[i])
    return smallest

def getBiggerOrEqual(array):
    bigger = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger.append(array[i])
    return bigger