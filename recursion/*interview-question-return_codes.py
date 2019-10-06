# We start with the number 143

# 1- Since number != 0 we move on
# 2- remainder = 143 % 100 -> 43
# 3- output_100 = list()
# 4- remainder is greater than 26 so move on
# 5- remainder = 143 % 10 = 3
# 6- output_10 becomes all_code(143 // 10) -> 14
# 7-    all_codes(14)
# 8-    remainder = 14 % 100 -> 14
# 9-    remainder is less than 26 and greater than 9
# 10-       output_100 becomes 14 // 100 -> 0
# 11-           all_code(0) returns [""]
# 12-           alphabet becomes get_alphabet(14) -> n
# 13-           output_100[index] becomes ["n"]
# 14-           remainder = 14 % 10 -> 4
# 15-           output_10 becomes 14 // 10 -> all_codes(1)
# 16-               all_codes(1) becomes output_10 -> 1/10-> 0 all_codes(0) which returns ['']
# 17-           for index, element in enumerate(output_10)
# 18-           output_10[index] = 'd'
# 19-           


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
    #
    for index, element in enumerate(output_10):
        
        output_10[index] = element + alphabet
        
    output = list()
    output.extend(output_100)
    output.extend(output_10)
    print(output)
    
    
    
    
    return output

print(all_codes(143))