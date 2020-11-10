import math
#Time Complexity O(n!)
#Optimization O(n!/(n-k!))
#Space Complexity O(n!/(n-k!))
def permutations(n, k):
    total_sum = sum([i for i in range(1, n + 1)])
    res = []

    def backtracking(current_permutation, permutation_sum):
        if len(current_permutation) == k:
            remainder = total_sum - permutation_sum
            if permutation_sum > remainder:
                res.append(math.factorial(n - k))
            return
        for i in range(1, n + 1):
            new_permutation = current_permutation + [i]
            current_sum = permutation_sum + i
            if i not in current_permutation:
                backtracking(new_permutation, current_sum)

    backtracking([], 0)
    return len(res)
print(permutations(3, 2))