

#Time complexity O(n*m)
#Iterating through the coins and iterating through the amounts
#The comparison is O(1) operation since we are only doing constant time operations
#Space complexity O(n) since we are creating an array for holding the target amounts uptill the target

def minNumberCoinsForChange(n, coins):

    #1- create an empty array that has all sub-problems

    numofcoins = [float("inf") for amount in range(n + 1)]

    #Set up the first subproblem for finding change of $0 to be 0 different coin ways
    numofcoins[0] = 0

    #Traverse through the denominations
    for coin of coins:
        #Traverse through the numOfcoins array
        for amount in range(len(numofcoins)):
            #Check if coin is less than the target amount
            #If it is , get the lower value of its existing value or the minimum of target i.e lets say 5 - the coin
            #We add the +1 so that we can always have one more way that was the 
            if coin <= amount:
                numofcoins[amount] = min(numofcoins[amount], numofcoins[amount - coin] + 1)
    
    return numofcoins[n] if numofcoins[n] != float('inf') else - 1