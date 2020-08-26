def find_valley(array):
    i = 0
    while i < len(array):
        while i < len(array) and array[i] <= array[i + 1]:
            i += 1
        valley = array[i]
        i += 1
    return valley

print(find_valley([9,7,6]))