
#Find the minimum value in the sub-array
#   [11,171,2,98,3,45,41,76,51,12,14,36]

#Find the maximum value in the array

def local_maxima_minima(array):
    minimum = float('inf')
    maximum = float('-inf')

    for i in range(len(array)):
        num = array[i]

        minimum = min(minimum, num)
        maximum = max(maximum, num)

    return maximum

#We can check if a number is out of order if it is smaller than previous number
#We can check if a number is out of order if it is larger than the next number
def number_out_of_order(index, num, array):
    if index == 0:
        return num > array[index + 1]

    if index == len(array) - 1:
        return num < array[index - 1]
    
    return num < array[index - 1] or num > array[index + 1]

#Compare number from left to right
def find_sorted_left_position(array, num):

    leftIdx = 0
    while num > array[leftIdx]:
        leftIdx += 1
    return leftIdx

def find_sorted_right_position(array, num):
    rightIdx = len(array) - 1
    while num < array[rightIdx]:
        rightIdx += 1
    return rightIdx



            