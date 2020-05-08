
#TIme Complexity O(N log N + M log M)
#Iterating over each array requires O(N) and thus doesn't impact our run time of log n
#Space Complexity of O(1) since sorting done in place

def smallest_difference(array1, array2):
    array1.sort()
    array2.sort()
    smallest_difference = float('inf')
    current_difference = float('inf')
    smallest_pair = []
    idxOne = 0
    idxTwo = 0

    while idxOne < len(array1) and idxTwo < len(array2):
        firstNumber = array1[idxOne]
        secondNumber = array2[idxTwo]

        if firstNumber < secondNumber:
            current_difference = secondNumber - firstNumber
            idxOne += 1

        elif firstNumber > secondNumber:
            current_difference = firstNumber - secondNumber
            idxTwo += 1

        else:
            return [firstNumber, secondNumber]

        if current_difference < smallest_difference:
            smallest_difference = current_difference
            smallest_pair = [firstNumber, secondNumber]
    return smallest_pair
    


print(smallest_difference([-1,5,10,20,28,3],[26,134,135,15,17]))