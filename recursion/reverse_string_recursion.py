#The goal in this notebook will be to get practice with a problem that is frequently solved by recursion: Reversing a string.

def reverse_string(input_string):

    #Base case
    #Stop the loop when you have iterated through each element of the input string
    #
    if len(input_string) == 0:
        return ''
    else:
        first_character = input_string[0]
        sub_string = input_string[1:]
        reversed_string = reverse_string(sub_string)
        return reversed_string + first_character

#Iteration 1
    #Iteration 2
        #Iteration 3
            #Iteration 4
                #Iteration 5
                    #Iteration 6
                        # len(input_string) == 0:
                            # return ''
#                 Return to Iteration 5
#             Return to Iteration 4
#         Return to Iteration 3
#     Return to Iteration 2
# Return to Iteration 1


#   Iteration 1:
#Lets start with the function
#In our first iteration we have input_string = 'aabbcc'
#First_character becomes a
#Substring becomes abbcc
#When we run reversed_string we run the function again without returning anything. So this continues to Iteration 2

#   Iteration 2:
#First character now becomes a
#Sub_string becomes bbcc
#When we run reversed_string we run the function again without returning anything. So this continues to Iteration 3

#   Iteration 3:
#First character becomes b
#Sub_string becokmes bcc
#When we run reversed_string we run the function again without returning anything. So this continues to Iteration 4

#   Iteration 4:
#First character becomes b
#Sub_string becokmes cc
#When we run reversed_string we run the function again without returning anything. So this continues to Iteration 5

#   Iteration 5:
#First character becomes c
#Sub_string becokmes c
#When we run reversed_string we run the function again without returning anything. So this continues to Iteration 6

#   Iteration 6:
#First character becomes c
#Sub_string becokmes NULL or len(input_string) is 0
#When we run reversed_string , we return '' and first character as c

# Then we continue back up to Iteration 5
# We return c and the first character so the reversed_string becomes cc

# Then we continue back up to Iteration 4
# We return cc and the first character which is b

# Then we continue back up to Iteration 3
# We return ccb and the first character which is b

# Then we continue back up to Iteration 2
# We return ccbb and the first character which is a

# Then we continue back up to Iteration 1
# We return ccbba and the first character which is a

# Therefore our final string becomes ccbbaa


print(reverse_string('aabbcc'))
print(reverse_string('abcdefgh'))