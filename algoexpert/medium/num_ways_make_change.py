# Dyanmic Programming 
# Number of ways to make change

#Base case - When making change for 0, there is only one way and that is to not offer any change
#            This can be done by making no change and buying it for free.


def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n + 1)]
    print('ways is ', ways)
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    
    return ways[n]


print(numberOfWaysToMakeChange(10, [1,5,10,25]))