#Caching can be defined as the process of storing data into a temporary data storage to
#avoid recomputation or to avoid reading the data from a relatively slower part of memory
#again and again

#Lets use caching to chalk out an efficient solution for a problem

#   In the staircase problem, we use recursion to compute by using only three defined base cases
#   We know that if the staircase is 1, we can take 1 step
#   If the staircase is 2, we can take 1 + 1 step, or take 2 steps together, so total solutions are 2
#   If the staircase is 3, we can take 1 + 1 + 1, 1 + 2, 2 + 1, and finally 3 steps, so total solutions are 4



def staircase(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

print(staircase(5))

#Now we are going to use a cache to store our results

#While using recursion for the above problem, you might have noticed a small problem with efficiency.

# Let's take a look at an example.
# Say the total number of steps are 5. This means that we will have to call at (n=4), (n=3), and (n=2)
# To calculate the answer for n=4, we would have to call (n=3), (n=2) and (n=1)
# You can notice that even for a small number of staircases (here 5), we are calling n=3 and n=2 multiple times. 
# Each time we call a method, additional time is required to calculate the solution. 
# In contrast, instead of calling on a particular value of n again and again, we can calculate it once and store the result to speed up our program.

#We start with staircase 4
#num_dict is an emtpy dict
def staircase(n):
    num_dict = dict({})
    return staircase_faster(n, num_dict)

#   Since n is 4, we go to first else 
#   since 3 is not in num_dict, we recurse
#   staircase_faster(3, num_dict)
#   staircase_faster(3, num_dict) -> output = 4
#   first_output = 4

#   since 2 is not in num_dict, we recurse
#   staircase_faster(2, num_dict)
#   staircase_faster(3, num_dict) - > output = 2
#   since 1 is not in num_dict, we recurse
#   staircase_faster(1, num_dict)
#   staircase_faster(1, num_dict) -> output == 1
#   output = 4 + 2 + 1
#   num_dict[4] -> 7
#   return output
#   This way now each time we have n == 4, we can display 7
#   Instead of recursing again and again, we can find the value at num_dict[4] and display it as first_output

def staircase_faster(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output = staircase_faster(n - 1, num_dict)

        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)

        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)
        
        output = first_output + second_output + third_output
    
    num_dict[n] = output;
    return output

print(staircase(4))