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

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]

        if paren in '{[(':
            stack.push(paren)
        else:
            if stack.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if is_matched(top, paren) == False:
                    is_balanced = False
        index += 1

    if stack.is_empty() and is_balanced:
        return True
    else:
        return False
