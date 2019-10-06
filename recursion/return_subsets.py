def subsets(arr):
    return return_subsets(arr, 0)

def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)
    print(small_output)
    #small_output becomes [[]]

    output = list()
    # append existing subsets
    for element in small_output:
        #Iterate over [], then [2]
        output.append(element)
    
    #output becomes [[],[2]]

    # add current elements to existing subsets and add them to the output
    for element in small_output:
        
        current = list()
        current.append(arr[index])
        
        #current becomes [[1]]
        current.extend(element)
        print(current)
        #current.extend(element) -> [[1], []]
     
        output.append(current)
        
    return output
    
print(subsets([1,2]))

#               
#             
#           []
#          / 
#         /     
#       []
#      /  \     
#     /    \   
#    /      [2]
#   /          
#  /            
#[]            
#  \            
#   \          
#    \      [1]
#     \    /   
#      \  /     
#       [1]
#         \       
#          \     
#           [1,2]
#                
#                 

# The idea of the subsets problem is to break the problem down into sub sets for each number
# We start with an empty subset []
# We then ask ourselves to either add the first number or skip it
# We are given two choices if we skip [] and if we add first number in case of [1,2] then [1]
# Then we have [] and [1]
# Then we create subsets from each [] and [1]
# If we skip it becomes [] -> []
# Then from each of these two elements we decide whether to add the next element at index [] add 2 becomes [] -> [2]
# If we skip it becomes [1] -> [1]
# If we add 2 it becomes [1] -> [1,2]
# So in total we are left with [], [2], [1], [1,2]

#In our algorithm, we start with the given array and start at index 0
#We then recurse
# We have a base case where if the index becomes larger or equal to the length of the given array
# That means we have searched through each element of the given array and we dont need to continue
# In that case we return [[]] an empty array within an array since if we are on index 3 and len is 2 then we are left with only the subset []

# In the first case, we start with index 0, then recurse the function with index + 1
# Our goal is to reach the far end of the algorithm to find the base case
# We will return with the base case of the empty subset first
# Then we start iterating on it
# For element in the base case which is []
# We create an output list for all our subsets and add this to our output which now becomes [[]]
# Then we come back one step and create another list
# This list will contain elements from the given array at the current index
# In our case since we go depth first first, so we after the base case, we find the value of current array at final index which is [2]
# We then add this to our existing output which now becomes [[], [2]]

# Next we come back one step and on the first value of the array
# Here the value of the array at index is 1
# So we create an empty list and iterate through the values in our iterations uptil now which are [[],[2]]

# Now we create a new list
# Add the element at given index value which is 1
# And we extend the values from the previous iterations
# 
# NOTE HERE THAT EXTEND MEANS TO ITERATE OVER THE VALUES e.g [1,2] returns 1,2. Append [4,5] means to add it as is to an existing array which can be [1,2,[4,5]]
# Extend iterates over the input and finds the element value and adds that to the given array
# In our case since [] has no element we just add the [1] value and append it to our output which now becomes [[],[2],[1]]
# Then for the second value which is 2, first we add the element at existing index which is 1 to our created list which becomes [1]
# Then we append 2 to it so it becomes [1,2]
# Then we append this to our output which now becomes [[],[2],[1],[1,2]]
