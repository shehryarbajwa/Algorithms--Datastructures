# Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. 
# In how many possible ways can you climb the staircase if the staircase has n steps? 
# Write a recursive function to solve the problem.

# Example:

# n = 3
# output = 4
# The output is 4 because there are four ways we can climb the staircase:

# 1. 1 step +  1 step + 1 step
# 2. 1 step + 2 steps 
# 3. 2 steps + 1 step
# 4. 3 steps

def staircase(n):

    if n <= 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return staircase(n-1) + staircase(n-2) + staircase(n-3)

print(staircase(5))

print(staircase(7))

#The idea behind this algorithm is very simple. You start with defining the answers to smaller problems
#We know that if there is 1 stair there is only one way to climb it
#We also know that if there are 2 stairs then there are two ways to climb it 1 + 1 or take 2 steps
#We also know that if there are 3 stairs then there are 4 ways to climb it

#1 + 1 + 1
#1 + 2
#2 + 1
#3

#Therefore all the problems can be solved by breaking down the n into smaller sub problems

# Think of it this way. If there are 13 stairs to climb
# We can add the answers from how many different choices we can make to climb first 4 stairs, then the next 4 stairs, then the next 3 stairs, then the next 2 stairs
# Or we can climb 4 stairs then 3 stairs then 3 stairs then 3 stairs
# Thus if we know the max it takes to climb 1,2 and 3 stairs, we can find how much time it will take by adding the sub problems together
