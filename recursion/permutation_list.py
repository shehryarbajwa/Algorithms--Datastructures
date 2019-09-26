# Let's use recursion to help us solve this permutation problem:

# Given a list of items, the goal is to find all of the permutations of that list. 
# For example, if given a list like: ["apple", "water"] you could create two permuations from it. 
# One in the form of the original input and one in the reversed order like so: ["water","apple"]

import copy

def permute(l):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      l(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item be represented by a list
    """
    

    perm = []
    if len(l) == 0:
        perm.append([])
    else:
        first_element = l[0]
        after_first = slice(1, None)
        sub_permutes = permute(l[after_first])
        
        print(sub_permutes)
        for p in sub_permutes:
            
            for j in range(0, len(p) + 1):
                r = copy.deepcopy(p)
                r.insert(j, first_element)
                perm.append(r)
    return perm

print(permute([1,0]))

#Lets take a look at this recursive function

# We provide the input of [1,0]

#permute([1,0])
# perm = []
# first_element = 1
# sub_permutes = permute([0])

    #permute([0])
    #perm = []
    #first_element = 0
    #sub_permutes = permutes([])

        #permute([])
        #perm = []
        #first_element is None
        #len(input) is 0, so perm = [[]]

    #Moving back to permute[[0]]
    #First_element is 0
    #We move to the for loop
    #for p in sub_permutes: sub_permutes = [[]]
        #p -> []
        #for j in range(0, len(p) + 1):
        #create a copy of [] which equals r
        #The loop runs 1 time
        #In the only 0th iteration
        #r.insert(0, first_element = 0) -> [0]
        
#Moving finally to permute[[1,0]]
#perm = []
#first_element = 1
#sub_permutes = [[0]]

#for p in sub_permutes -> [0]
#for j in range(0, len(p) + 1): 
#len(p) -> 1
#Loop runs 2 times - 0 and 1
#In the 0th iteration
#r = copy.deepcopy(p) -> [0]
#r.insert(0, 1) -> [1,0]
#perm.append(r) -> perm becomes [[1,0]]
#Then in the 1th iteration:
#r = copy.deepcopy(p) -> [0]
#r.insert(1, first_element) -> [0,1]
#perm.append(r) -> perm becomes [[1,0], [0,1]]