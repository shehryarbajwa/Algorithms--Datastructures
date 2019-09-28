# Define a procedure, deep_reverse, that takes as input a list, and returns a new list that is the deep reverse of the input list.
# This means it reverses all the elements in the list, and if any of those elements are lists themselves, reverses all the elements in the inner list, all the way down.



def is_list(element):
    """
    Check if element is a Python list
    """
    return isinstance(element, list)

def deep_reverse(arr):
    """
    Function to deep_reverse an input list
    """
    return deep_reverse_func(arr, 0)

def deep_reverse_func(arr, index):
    """
    Recursive function to deep_reverse the input list
    """
    # Base Case
    if index == len(arr):
        return list()
    
    output = deep_reverse_func(arr, index + 1)
    
    # if element is a list --> deep_reverse the list
    if is_list(arr[index]):
        to_append = deep_reverse(arr[index])
    else:
        to_append = arr[index]
        
    output.append(to_append)
    return output

print(deep_reverse([1,2,[3,2],4]))


#   Lets start with the arr [1,2,[3,2],4]
#   We provide this array to deep_reverse function
#   Deep reverse runs a recursive deep_reverse_function with arr and index 0
#   Deep_reverse_func([1,2,[3,2],4], 0)
#   Element at index 0 is and is != len(arr)=4 so we continue
#   Output is a recursive step so we move on to deep_reverse_function(arr, 1)

#       We are on deep_reverse_function(arr, 1):
#       Len of index 1 is not equal to 4 so we continue
#       at output we run deep_reverse_function again with (arr,2)

#           We are on deep_reverse_function(arr,2)
#           Len of index 2 is not equal to 4 so we continue
#           output = deep_reverse_function(arr, 3)

#               We are on deep_reverse_function(arr, 3)
#               Len of index 3 is not equal to 4 so we continue
#               output = deep_reverse_function(arr, 4)

#                   We are on deep_reverse function(arr, 4)
#                   Len of index 4 is equal to len  of arr so we return an empty arr

#              We are back on deep_reverse_function(arr, 3)
#              We have an empty array
#              We check if the arr at current index is already an array
#              In this case since the arr at index value 3 is 4 so we use the else statement
#              to_append = arr[index]
#              Then we append it to output
#              Output's value from previous iteration is an empty array
#              Now that array becomes [4]

#           We come back on deep_reverse_function(arr,2)
#           ouput's result is [4]
#           arr's value at index 2 is [3,2]
#           We check if the arr[index] is an existing array
#           If it is, we run the deep_reverse(arr[index])
#           This will break down our list and run deep_reverse_function([3,2], 0)
#           So we start deep_reverse_function
#           Since index at 0 is not equal to len of arr which is 2, we keep going
#           output becomes deep_reverse_function([3,2],1)
#           Now we are running deep_reverse_function([3,2],1)
#           Since index at 1 != len which is 2
#           We continue, output becomes deep_reverse_function([3,2], 2)
#           Since index at 2 == len i.e 2, we create an empty list
#           We come back output is now []
#           [3,2] index at 1 is 2
#           to_append becomes arr[index] -> [3,2][1] -> 2
#           output which is [] is appended with 2 it becomes [2]
#           We move back one spot [3,2] at index 0 deep_reverse_function
#           Now output is [2]
#           We check if else
#           to_append becomes arr[0] -> 3
#           final output for this becomes [2,3]
#           Since we have run our is_list(arr[index]) we move back one iteration

#       We are back on deep_reverse_function(arr,1) 
#       Element of arr[1,2,[3,2],4] at index 1 is 2
#       output is [4,[2,3]]
#       to_append becomes 2
#       output becomes [4,[2,3],2]

#  We are back to our final deep_reverse_function(arr,0)
#  output is [4,[2,3],2]
#  to_append becomes arr[0] which is 1
#  output becomes [4,[2,3],2,1]
