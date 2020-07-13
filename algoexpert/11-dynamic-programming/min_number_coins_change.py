def min_number_coins_change(n,denoms):
    min_ways_to_make_change = [float('inf') for amount in range(n + 1)]
    min_ways_to_make_change[0] = 0

    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                min_ways_to_make_change[amount] = min(min_ways_to_make_change[amount], 1 + min_ways_to_make_change[amount - denom])

    return min_ways_to_make_change[n] if min_ways_to_make_change[n] != float('inf') else -1

