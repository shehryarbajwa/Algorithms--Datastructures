def permutations(array):

    def backtrack(array, current_permutation, total_permutations):
        if not array:
            total_permutations.append(current_permutation)
        else:
            for i in range(len(array)):
                new_array = array[:i] + array[i + 1:]
                new_permutation = current_permutation + [array[i]]
                backtrack(new_array, new_permutation, total_permutations)
    output = []
    backtrack(array, [], output)
    return output

print(permutations([1,2,3]))