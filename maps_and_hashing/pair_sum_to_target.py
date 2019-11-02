# Given an input_list and a target, return the indices of pair of integers in the list that sum to the target. 
# The best solution takes O(n) time. 
# You can assume that the list does not have any duplicates.

# For e.g. input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3]

# The idea is to create a dictionary where we store the index of the elements we iterate over the input_list
# If we find that the target - iterable element exists in the dictionary, we input that and the index 
# In our dictionary, we can store the index values of our elements
# For example in [1,5,9,7] in our dic we store dic[1] -> 0
#                                              dic[5] -> 1
#                                              dic[9] -> 2
#                                              dic[7] -> 3

def pair_to_sum_target(input_list, target):
    index_dict = dict()

    for index, element in enumerate(input_list):
        if target - element in index_dict:
            return [index_dict[target - element], index]
        index_dict[element] = index 

#   In our algorithm, when we are iterating over for index(3), element = 7
#   Our target is 8, and 8 - 7 = 1
#   since we have 1 in index_dict as a key value
#   