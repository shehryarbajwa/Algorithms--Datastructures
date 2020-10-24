#Time Complexity O(4^n * 3^n)
#Worst case is O(4^n) Average case is O(3^n)
#Space Complexity O(d) max height of the calls on the call stack

def letter_combinations(digits):
    if not digits:
        return []
    output = []
    recursive_letter_combination(digits, '', output)
    return output

def recursive_letter_combination(digits, current_string, output):
    #base case
    if len(digits) == 0:
        output.append(current_string)
        return
    
    characters = digit_to_letter(digits[0])
    for character in characters:
        current_string += character
        recursive_letter_combination(digits[1:], current_string, output)
        #backtrack, decrement the character added
        #move back up
        current_string = current_string[:-1]

def digit_to_letter(digit):
    mapping = {
        '2' :'abc',
        '3' :'def',
        '4' :'ghi',
        '5' :'jki',
        '6' :'mno',
        '7' :'pqrs',
        '8' :'tuv',
        '9' :'wxyz'
    }
    
    return mapping[digit]