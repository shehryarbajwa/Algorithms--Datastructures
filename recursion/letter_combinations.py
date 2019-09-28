# A keypad on a cellphone has alphabets for all numbers between 2 and 9.

# You can make different combinations of alphabets by pressing the numbers.

# For example, if you press 23, the following combinations are possible:

# ad, ae, af, bd, be, bf, cd, ce, cf

# Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2. Likewise, if the user types 32, the order would be

# da, db, dc, ea, eb, ec, fa, fb, fc

# Given an integer num, find out all the possible strings that can be made using digits of input num. Return these strings in a list. 
# The order of strings in the list does not matter. However, as stated earlier, the order of letters in a particular string matters.


def letter_combination(digits):

    phones = {
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n' , 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u' , 'v'],
        '9' : ['w', 'x', 'y', 'z']
    }

    def backtrack(combination, next_digits):

        if len(next_digits) == 0:
            
            output.append(combination)

        else:

            for letter in phones[next_digits[0]]:

                backtrack(combination + letter, next_digits[1:])

    output = []

    if digits is not None:
        backtrack("", digits)
    return output

print(letter_combination("234"))

#So what is happening in this algorithm
#We declare a letter_combination function that takes a string of digits i.e 123, 234 etc
#We create a dictionary which contains the digit along with the alpha values i.e 2 -> a,b,c
#Then we define the backtrack function
#The backtrack function takes a combination i.e ab, ac or none initially and the next digits
#The base case is if there are no next digits meaning we have reached the end of 234 i.e 4, we will just append the combnination to our output list
#Else

#Lets map it out. The idea is to create trees so e.g 2-a,b,c -2[a] -> d,e,f ,, 2[b]-> d,e,f ,, 2[c]-> d,e,f

#So lets start with 234
# 1-We declare the digits dictionary
# 2-Since digits is not None, we run backtrack with an empty string and the digits 234
# 3-We run backtrack("", 234)
# 4-Len of digits is not 0 so we continue
# 5-For letter in phones[2]: maps to a,b,c
# 6-We start with a
# 7-Then run backtrack again with backtrack("" + a, 3)

    #   Now we are in loop 1
    #   We are running backtrack(a, 3)
    #   Len of digits is not 0 so we continue
    #   For letter in phones[3]: maps to d,e,f
    #   We start with d
    #   Then run backtrack again with backtrack(a+d, 4)

        #   Now we are loop 2
        #   We are running backtrack(ad, 4)
        #   Len of digits is not 0 so we continue
        #   For letter in phones[4]: maps to g,h,i
        #   We start with g
        #   Then run backtrack again with backtrack(ad + g, None)

            # Now we are loop 3
            # Len of next_digits is None
            # So we exit the loop and append combination which is adg to our output list
            # We will keep doing this for each letter of our original loop 0 starting now with b and backtrack("" + b, 3)   