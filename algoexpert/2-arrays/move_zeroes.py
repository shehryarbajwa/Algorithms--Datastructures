
def move_zeroes(array):
    left = right = 0
    
    while right < len(array):
        if array[left] == 0:
            array.append(array.pop(left))
        else:
            left += 1
        right += 1
    return array

print(move_zeroes([0,0,1]))