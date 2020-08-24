

def flip_image(array):

    #reverse each row
    #O(N * M)
    #O(1) since not storing anything

    for i in range(len(array)):
        start_col = 0
        end_col = len(array[i]) - 1

        while start_col <= end_col:
            array[i][start_col], array[i][end_col] = array[i][end_col], array[i][start_col]
            start_col += 1
            end_col -= 1

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                array[i][j] = 1
            elif array[i][j] == 1:
                array[i][j] = 0
            else:
                continue
    return array

def flip_image_concise(array):

    for row in array:
        row.reverse()

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                array[i][j] = 1
            elif array[i][j] == 1:
                array[i][j] = 0
            else:
                continue

    return array

print(flip_image(
    [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    ))




