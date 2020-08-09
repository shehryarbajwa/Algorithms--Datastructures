def move_elements_to_end(array, to_move):
    for i in range(len(array)):
        if array[i] == to_move:
            num = array.pop(i)
            array.append(num)

    return array


print(move_elements_to_end([2,1,4,2,2,6], 2))