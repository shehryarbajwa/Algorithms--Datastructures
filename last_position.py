def last_pos(array, target):
    left = 0
    right = len(array) - 1

    while left + 1 < right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid
        else:
            right = mid

    #post-processing

