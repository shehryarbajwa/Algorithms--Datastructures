## Given an input array of integers, return a sorted array of the three largest integers in the input array.
## [10,10,12] from an input array of [10,5,9,10,12]
## E.g [1,2,3,4,5,6]
## [0,0,0]


## The problem we are solving is to traverse through the array of integers
## We need to return an array with the largest numbers in the provided array
## We traverse through the array and compare whether the iterator is larger than the largest, secondlargest, thirdLargest number
## We need to compare three numbers largest, secondlargest, thirdLargest
## When the value iterated is not greater than any value, we just break out of the loop

def findThreeLargestNumbers(array):
    largest = 0
    secondlargest = 0
    thirdlargest = 0
    largest_numbers = [thirdlargest, secondlargest, largest]
	
    for number in array:
        updateLargest(largest_numbers, number)
		
    return largest_numbers

def updateLargest(largest_numbers, number):
	
    if number > largest_numbers[2] or largest_numbers[2] is 0:
        shiftAndUpdate(largest_numbers, number, 2)
    elif number > largest_numbers[1] or largest_numbers[1] is 0:
        shiftAndUpdate(largest_numbers, number, 1)
    elif number > largest_numbers[0] or largest_numbers[0] is 0:
        shiftAndUpdate(largest_numbers, number, 0)
    else:
        shiftAndUpdate(largest_numbers, number, -1)

def shiftAndUpdate(largest_numbers, number, index):

    if index == -1:
        return
	
    for i in range(index + 1):
        if i == index:
            largest_numbers[i] = number
        else:
            largest_numbers[i] = largest_numbers[i + 1]
	

print(findThreeLargestNumbers([1, 2, 1, 0, 5, 9, 12]))
