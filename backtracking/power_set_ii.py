
def subsets_backtracking(array):
    array.sort()
    return subsets_backtracking_helper(array, idx=None)

def subsets_backtracking_helper(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    ele = array[idx]
    subsets = subsets_backtracking_helper(array, idx - 1)
    for i in range(len(subsets)):
        current_subset = subsets[i]
        subsets.append(current_subset + [ele])
    return subsets

print(subsets_backtracking([1,2,2]))

    
