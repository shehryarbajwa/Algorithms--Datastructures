##########  QUESTION TO ASK THE INTERVIEWER         ##################
##########  SHOULD TARGET - ELEMENT RETURN JUST 1 PAIR OR MULTIPLE ############


#### SO WHAT ARE WE DOING ####
#   We create an empty dictionary that will map elements(key) to their index in input_list(value)
#   This is doing the reverse of a usual dictionary where index maps to values
#   Here values map to index for an array
#   We will iterate over the original input_list via enumerate, index, element
#   We will then map the element of the input_list to its index in input_dict
#   input_dict[element] = index
#   While we are enumerating
#   If we find target - element , 5 - 2 = 3 exists in input_dict[key]
#   Since 3 is included in input_dict after 2 and has a value of 2
#   We will return index_dict[target - element] = 2, index we are iterating over 1
#   Then we will return the input_dict[element] against that value which is 
#   
#    {
#    '1':'0',
#    '2':'1',
#    '3':'2',
#    '4':'3'
#   }

#   








def pair_to_sum_target(input_list, target):
    index_dict = dict()

    for index, element in enumerate(input_list):
        if target - element in index_dict:
            return [index_dict[target - element], index]
        index_dict[element] = index 

print(pair_to_sum_target([1,5,9,7], 8))