


def is_monotonic(array):

    increasing_sequence = True
    decreasing_sequence = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            increasing_sequence = False
            

        if array[i] > array[i - 1]:
            decreasing_sequence = False
            

    return decreasing_sequence or increasing_sequence

def direction_of_array(array):

    increasing = True
    left = 0
    right = left + 1

    while increasing and right < len(array):
        if array[right] > array[left]:
            left += 1
            right += 1
        else:
            increasing = False
    return increasing
        

def iteration(array):
    new_arr = []
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            new_arr.append(array[i])
            new_arr.append(array[i - 1])

    return new_arr

print(iteration([1, 2, 3,4,5]))


print(is_monotonic([-1,-5,-10,-1100,-1101,-1102, -9001]))

print(direction_of_array([1, 5, 4, 1100, 1101, 1102, 9001]))