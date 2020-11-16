def combination_sum(array, target):
    output = []

    def backtrack(current_combination, current_sum, target):
        if current_sum > target:
            return
        if current_sum == target:
            if sorted(current_combination) not in output:
                output.append(current_combination)
        else:
            for num in array:
                new_combination = current_combination + [num]
                running_sum = current_sum + num
                backtrack(new_combination, running_sum, target)

    backtrack([], 0, target)
    return output

print(combination_sum([2,3,7], 7))