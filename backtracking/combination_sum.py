def combinations_sum(combinations, target):
    output = []

    def backtrack(current_sum, current_combination, target):
        if current_sum > target:
            return
        if current_sum == target:
            current_combination.sort()
            if current_combination not in output:
                output.append(current_combination)
        else:
            for num in combinations:
                new_combination = current_combination + [num]
                unique_sum = current_sum + num
                backtrack(unique_sum, new_combination, target)
    backtrack(0, [], target)
    return output

print(combinations_sum([2,3,6,7], 7))

