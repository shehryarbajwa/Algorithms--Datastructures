# Given an input string, return all permutations of the string in an array.

# Example 1:

# string = 'ab'
# output = ['ab', 'ba']
# Example 2:

# string = 'abc'
# output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

# This problem is similar in the input_list problem since the size of the output depends on the size of the input


def permutations(string):
    return return_permutations(string, 0)

def return_permutations(string, index):
    if index >= len(string):
        return ['']
    
    small_output = return_permutations(string, index + 1)
    

    output = list()
    current_char = string[index]
    

    for permutation in small_output:
        #We use small_output[0] to find out what is the length of each element in the array like bc and add 1 because the next permutation will be of 3 lettered string
        #same way if we have abc then next string will be 4 letters
        for index in range(len(small_output[0]) + 1):
            new_permutation = permutation[0: index] + current_char + permutation[index:]
            print(new_permutation)
            output.append(new_permutation)
    return output

print(permutations('abb'))


#We start with the permutations function by providing it the string abc
#It starts the recursion on abc, index 0
#small_output = runs the recursion again but with the index + 1 so the purpose it to keep moving till the end of string to recurse then back up
#We finish the recursion at abc, index 3 since 3 >= len(abc) = 3 = 3 so return [''] empty list

    #small_output becomes ['']
    #current_character is string[index] -> abc[2] -> c
    #Since there are no permutations in small_output just an empty list we iterate over that
    #index in range(len(small_output[0] + 1)) -> the range is 0 + 1 -> 1
    #index is 0
    #We take the element from 0 till the index 
    #we take the current element which is c
    #We take the element from index till the end of the list which is also nill
    #so our list becomes ['c']

        #Then we move to the previous loop
        #our small_output is ['c']
        #current_character is abc[1] -> b
        #range is len(small_output[0]) -> 1 and add 1 
        #index runs from 0 and 1
        #Element from 0 till index at 0 is null
        #Element after it is b
        #Element after [0:] is c
        #So in index interation it becomes bc

        #Then we run index 1
        #Elemnent from 0 till index 1 is c
        #current character is b
        #element after index 1 is Null
        #so in index iteration it becomes cb

        #Thus in this loop, our small_output becomes bc, cb

            #Then we move to our final loop i.e the first_iteration of return_permutation
            #current_char is abc[0] -> a
            #permutation in small_output are bc, cb so two
            #we iterate through bc first then cb
            #for index in range(len(small_output[0] + 1)) small_output[0] is bc and its length is 2 so range is 3
            #index values are 0, 1, 2
            #Element from 0 till index 0 is Null
            #current character is a
            #Element from [0:] is bc
            #So our permutation becomes abc

            #Next element from [0:1] is b
            #current_char is a
            #Element from [1:] is c
            #So our permutation becomes bac

            #Next element from [0:2] is from 0 till elem at index 2 is bc
            #current_char is a
            #next_element at [2:] is Null
            #so our permutation becomes bca

            #Then we start our second iteration of small_output which is cb
            #Current_char is a

            #Index in range - range is 3
            #index values are 0,1,2
            #Element at index[0:0] is null
            #Current_char is a
            #Element from [0:] is cb
            #So permutation becomes cba

            #Element at index[0:1] is c
            #current_char is a
            #Element at [1:] is b
            #our Permutation becomes cab

            #Element at index[0:2] is cb
            #Current_char is a
            #Element at [2:] is Null
            #So our permutation becomes cba

            #We can see a pattern. 
                
                
                                        #Technically what we are doing is this
                                        # iterate over each permutation string received thus far
                                        # and place the current character at between different indices of the string 



