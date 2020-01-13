
# Time Complexity O(N^2) Worst and Average
# Time Complexity O(N) if already sorted
# Insertion sort works by creating two sub-arrays one sorted and one unsorted

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[i] < array[j - 1]:
            swap(i, j - 1, array)
            j -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]