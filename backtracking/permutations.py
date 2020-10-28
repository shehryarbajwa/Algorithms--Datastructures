






#Recursion
#Time Complexity O(n!*n*n) -> n! for base case, n for iterating over elements, n for slicing array and concatenating array i.e n + n but comes to n
#Space Complexity O(n!*n) -> n! for base case, n for creating new arrays
def permutations_recursive(array):
    permutations = []
    permutations_helper(array, [], permutations)
    return permutations

def permutations_helper(array, current_permutation, permutations):
    if not len(array) and len(current_permutation):
        permutations.append(current_permutation)
    else:
        for i in range(len(array)):
            #Remove num
            new_array = array[:i] + array[i + 1:]
            new_permutation = current_permutation + [array[i]]
            permutations_helper(new_array, new_permutation, permutations)


#Backtracking
#Time Complexity O(n!*n)
#Space Complexity O(n!*n) -> All operations done in place, no new arrays created
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