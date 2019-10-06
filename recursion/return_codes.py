
# The idea behind the algorithm is very simple and in two steps
# We start with the base case
# If the input number is a 0, then there are no variations of this and we return [""]
# Our goal is to keep reducing the number in two fashions. One where we take two right most digits
# Second to take the right most digit
# If the remainder of the input number is divisible by 100, and the remainder has 2 digits
#   We program a logic to see if the remainder is <= 26 and > 9
#   If that is the case, then it is possible that the character can be two digits but represent one value e.g 10 represents j
#   We take the remainder and get the codes for the remaining numbers. In 123, remainder is 23, so we take 23 and then run recursion
#   Recursively we want to find the codes for 1. To achieve that we do 123 // 100 gives us 1.
#   Then we run the program again and find the remainder of the codes for 1
# The second logic we need is if we take 1 number to represent 2 digits, the second number is a single digit so we need to return one character against it
# This will be achieved by taking another remainder
# This time we want to find the right most value so 123 % 10 -> 3
# The remainder will be saved, and we will try to recurse to get the codes for 12 by 123 // 10 -> 12
# There is a clear pattern. We are trying to check two things
# 1-Whether the number can have multiple digits but represent one value
# 2-If the above is not true, then we check the digit one by one on each case
# 
# We keep taking out remainders one digit or two and keep dividing the problem into smaller subproblems
# 1123 we take out 23 and recurse on 11
# 1123 we take out 3 and recurse of 3

#In this specific algorithm, it is important to mention that output becomes merged from both into one as we iteratively come back to our original function
#Even though they start out as two different arrays of outputs, they end up adding same values to each of their element and index
#In the end they coalesce into one larger array

def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember: 
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)

def all_codes(number):
    if number == 0:
        return [""]
    
    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    if remainder <= 26 and number > 9 :
        
        # get all codes for the remaining number
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(remainder)
        
        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet
            
    
    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10
    # get all codes for the remaining number
    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(remainder)
    
    
    #In the final step, at this stage, the output being received for output_10 is [n, ad]
    # since we iterate over each index
    # at output_10[0] = n + c
    # at output_10[1] = ad + c
    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet
        
    output = list()
    output.extend(output_100)
    output.extend(output_10)
    print(output)
    return output

print(all_codes(1123))

