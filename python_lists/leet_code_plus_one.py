"""
Problem Statement
You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [9, 9, 9]
output = [1, 0, 0, 0]
Challenge:

One way to solve this problem is to convert the input array into a number and then add one to it. For example, if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits of the output number 124.

But can you solve it in some other way?
"""

class Solution(object):
    def plusOne(self, input_numbers):
        
        #If the last digit of the list is less than 9, increment that number by one
        if input_numbers[-1] < 9:
            input_numbers[-1] = input_numbers[-1] + 1
        else:
        #If the length of the list is 1, our input digit is 9, then we return a list with the incremented number
            if len(input_numbers) == 1:
                input_numbers = [1,0]
            else:
            #If the length of the list is greater than 1 and the input digit is 9
            #We provide a new array to our function with the last number excluded and add 0 to the input numbers at the end
                input_numbers = self.plusOne(input_numbers[:-1]) + [0]
        return input_numbers
test = Solution()
num1 = [1,9]
print( test.plusOne(num1))