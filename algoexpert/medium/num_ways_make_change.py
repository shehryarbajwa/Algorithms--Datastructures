# Dyanmic Programming 
# Number of ways to make change

#Base case - When making change for 0, there is only one way and that is to not offer any change
#            This can be done by making no change and buying it for free.

## Hint: Build up the array one coin denomination at a time. In other words, find the number of ways to make change for all amounts between 0 and n.
## Basically iterate over the target array called ways.
## At each list item, iterate over the denomination, and if the denomination is equal to the amount, then increment that array with the difference between amount and denom.

# ways = _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# this   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12


def numberofwaystomakechange(target, array):

    ways = [0 for amount in range(target + 1)]
    ways[0] = 1

    for denom in array:
        for amount in range(1, target + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[target]

