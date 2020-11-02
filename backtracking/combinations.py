#Time Complexity O(K * NCK) - k for hitting base case, NCK for selecting 4Combination 2 selections
#Space Complexity O(NCK) - storing base case
def combinations(n, k):
    output = []
    def backtrack(start, current_combination):
        if len(current_combination) == k:
            output.append(current_combination)
        else:
            for i in range(start, n + 1):
                current = current_combination + [i]
                backtrack(i + start, current)
    backtrack(1, [])
    return output

print(combinations(4, 2))