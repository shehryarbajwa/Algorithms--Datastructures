
#Conditions

# 1     2       3      4
# 5     6       7      8
# 9     10      11     12
# 13    14      15     16

def zigzag_traverse(array):
    #Determine the matrix bounds
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []

    current_row, current_col = 0,0
    goingDown = True

    while is_out_of_bounds(current_row, current_col, height, width) == False:
        result.append(array[current_row][current_col])
        if goingDown:
            #Only if the current col is 0 or row is last row we stop moving down
            #If It is the last row first column, we move right
            #Otherwise we just move one row down
            if current_col == 0 or current_row == height:
                goingDown = False
                if current_row == height:
                    current_col += 1
                else:
                    current_row += 1
            else:
                current_row += 1
                current_col -= 1
        else:
            if current_row == 0 or current_col == width:
                goingDown = True
                if current_col == width:
                    current_row += 1
                else:
                    current_col += 1
                pass
            else:
                current_row -= 1
                current_col += 1

    return result

def is_out_of_bounds(current_row, current_col, height, width):
    return current_row > height or current_row < 0 or current_col < 0 or current_col > width

print(zigzag_traverse([[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]))