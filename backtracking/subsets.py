#Time Complexity O(2^n * n / 2) -> 2^n for all subsets, n for each subset's average length
#Space Complexity O(2^n * n/2)
def subsets(array):
    subsets = [[]]
    for num in array:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [num])
    return subsets

def subsets_backtracking(array):
    
    def helper(idx, current_subset, subsets):
        
        subsets.append(current_subset[:])

        for i in range(idx, len(array)):

            element = array[i]
            helper(i + 1, current_subset + [element], subsets)

    subsets = []
    helper(0, [], subsets)
    return subsets

print('backtracked', subsets_backtracking([1,2,3]))
print(subsets([1,2,3]))
