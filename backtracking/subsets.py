#Time Complexity O(2^n * n / 2) -> 2^n for all subsets, n for each subset's average length
#Space Complexity O(2^n * n/2)
def subsets(array):
    subsets = [[]]
    for num in array:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [num])
    return subsets

print(subsets([1,2,3]))
