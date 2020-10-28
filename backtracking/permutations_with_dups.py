#Sorting is nlogn 
#Time Complexity O(n!*n*n)
#Space Complexity O(n!*n) -> n! appends and n recursive calls on the call stack
def permutations_with_dups(array):
    array.sort()
    permutations = []
    permutations_helper(array, [], permutations)
    return permutations

def permutations_helper(array, current_permutation, permutations):
    if not array:
        permutations.append(current_permutation)
    else:
        for i in range(len(array)):
            if i > 0 and array[i] == array[i-1]:
                continue
            new_array = array[:i] + array[i + 1:]
            new_permutation = current_permutation + [array[i]]
            permutations_helper(new_array, new_permutation, permutations)


print(permutations_with_dups([1,1,2,3]))



