def find_peak(array):
    i = 0
    peak = 0
    while i < len(array) - 1:
        while i < len(array) and array[i] <= array[i + 1]:
            i += 1
        peak = array[i]
        i += 1
    return peak

print(find_peak([1,2,3,4,5,6,7,8,9,0]))

