def num_ways_to_make_change(n, denoms):
    ways = [0 for amount in range(n + 1)]
    ways[1] = 0

    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[n]