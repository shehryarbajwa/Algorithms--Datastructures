#Go through elements side by side.
#Compare first element with the second element
#If first is bigger, switch
#Keep moving on doing it for each element

#Compare elements in the array side by side and switch

# Iteration #           1       2       3       4
# # of comparisons     n-1      n-1     n-1    n-1

#Efficiency (n-1)*(n-1) = n^2 - 2n + 1
#Thus efficiency is O(n^2)

#Worst case is O(n^2)
#Average case is O(n^2)
#Best case can be O(n)
#This can be when the array is already sorted
#Or when just 1 element needs to be sorted
#Space complexity is O(1)

