def rotate_image(matrix):
    size = len(matrix)
    layers = size // 2

    for layer in range(layers):
        first = layer
        last = size - first - 1

        for element in range(first, last):
            offset = element - first

            top = matrix[first][element]
            right_side = matrix[element][last]
            bottom = matrix[last][last-offset]
            left_side = matrix[last-offset][first]

            matrix[first][element] = left_side
            matrix[element][last] = top
            matrix[last][last-offset] = right_side
            matrix[last-offset][first] = bottom
    return matrix
print(rotate_image([
  [1,2,3],[4,5,6],[7,8,9]
]))