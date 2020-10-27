

#Backtracking
#Time Complexity O(n!*n)
#Space Complexity O(n!*n)
def permutations(array):
    perms = []
    permutation_helper(0, array, perms)
    return perms

def permutation_helper(index, array, permutations):
    if index == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(index, len(array)):
            swap(index, j, array)
            permutation_helper(index + 1, array, permutations)
            swap(index, j, array)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]