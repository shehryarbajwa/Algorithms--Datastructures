def first_and_last(array, target):
    output = []

    def find_first(array, target, output):

        left = 0
        right = len(array) - 1

        while left + 1 < right:

            mid = (left + right) // 2

            if array[mid] == target:
                right = mid

            elif array[mid] < target:
                left = mid
            else:
                right = mid
        
        if array[left] == target:
            output.append(left)
        elif array[right] == target:
            output.append(right)
        else:
            output.append(-1)
    

    def last_index(array, target, output):
        left = 0
        right = len(array) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if array[mid] == target:
                left = mid
            elif array[mid] < target:
                left = mid
            else:
                right = mid
        
        if array[right] == target:
            output.append(right)
        elif array[left] == target:
            output.append(left)
        else:
            output.append(-1)

    find_first(array, target, output)
    last_index(array, target, output)
    return output

print(first_and_last([1,2,2,3,4,5,6], 2))
    
