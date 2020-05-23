
#Time Complexity O(N)
#Space Complexity O(N)

#Edge case - 1 ]() , ()()]] - Where we have input that has a closing bracket but no equivalent opening bracket
#                             The way to check this is to see if the stack is empty. If it is empty, it means that there is no equivalent opening bracket

#Edge case - 2 We encounter a closing bracket but it has no equivalent opening bracket in the stack

#           We encounter a } but last opening bracket is ( so we return False

def balanced_brackets(string):
    stack = []
    opening = '([{'
    closing = ')]}'
    pairs = {'(': ')', '[': ']', '{': '}'}


    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            opening_bracket = stack[-1]
            if char == pairs[opening_bracket]:
                stack.pop()
            else:
                return False
    
    return True if len(stack) == 0 else False


print(balanced_brackets('([])(){}(())()()'))