def power_set(array):
    subsets = [[]]
    
    for char in array:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [char])
    return subsets

print(power_set([1,2]))