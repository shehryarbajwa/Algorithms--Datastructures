# [7,1,4,6,9,22,1]

# max_profit 

def best_time_to_buy(array):
    i = 0
    peak = array[0]
    valley = array[0]
    max_profit = 0

    while i < len(array) - 1:
        while i < len(array) - 1 and array[i] >= array[i + 1]:
            i += 1
        valley = array[i]

        while i < len(array) - 1 and array[i] <= array[i + 1]:
            i += 1
        peak = array[i]

        max_profit += peak - valley

    return max_profit

print(best_time_to_buy([7,1,4,6,9,22,1]))

