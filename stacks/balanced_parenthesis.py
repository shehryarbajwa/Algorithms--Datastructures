#Use stacks to make sure that the parenthesis are balanced in mathematical expressions

class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

#Examples = {()}
#Example 2 = (()
#Example 3 = ))
#Example 4 for else case ))){()}((( - in this case it is already not balanced
#Example 5 = {{{()}}}
#We assume that any string starting with a closing parenthesis is not balanced
#Since that follows English syntax that is the case


def is_matched(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False

def is_balanced_paren(paren_string):

    index = 0
    stack = Stack()
    is_balanced = True
    #Check if is_balanced boolean is true while the input string is being looped over

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        #If the parenthesis being looped over belongs to {[(
        #Push the parenthesis on the stack
        if paren in '{[(':
            stack.push(paren)
        #If the one being looped over is a closing parenthesis
        else:
        #First check if the stack is empty
        #The stack will be empty if we start with a closing parenthesis
        #If we start with a closing parenthesis, it is not balanced and we can exit the loop

            if stack.is_empty():
                is_balanced = False
        #If the stack is not empty, meaning we added some elements before like ((( and now we have )
        #then pop the top element of the stack and compare
        #The compare method will check if the closing bracket and the last item are the same
        #If they are the same, keep going through the loop
        #If they are not, it is not balanced and exit the loop
        #increment the index and move forward
            else:
                top = stack.pop()
                if is_matched(top, paren) == False:
                    is_balanced = False
        index += 1
    #Once we have compared all elements, each we pop the element, we reduce the stack
    #Once the stack is empty and it is still balanced, that means, the input string has equal opening and closing brackets
    #If that is not the case, return False
    if stack.is_empty() and is_balanced:
        return True
    else:
        return False

print(is_balanced_paren('(()'))
print(is_balanced_paren('(())'))
print(is_balanced_paren('(()))'))
print(is_balanced_paren('(()[][]{})'))
print(is_balanced_paren('(()'))
