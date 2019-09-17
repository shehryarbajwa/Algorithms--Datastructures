class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1
    
    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head.value
            self.head = self.head.next
            self.num_elements -= 1
            return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

#We iterate through the input array or list
#If it is a number, we add that to the stack
#If it is an arithmetic operation, we remove the last two numbers from the stack
#We do the arithmetic on them and push the result to the stack
#
def evaluate_post_fix(input_list):
    stack = Stack()
    for element in input_list:
        if element == '*':
            second = stack.pop()
            first = stack.pop()
            output = first * second
            stack.push(output)
        elif element == '/':
            second = stack.pop()
            first = stack.pop()
            output = int(first / second)
            stack.push(output)
        elif element == '+':
            second = stack.pop()
            first = stack.pop()
            output = first + second
            stack.push(output)
        elif element == '-':
            second = stack.pop()
            first = stack.pop()
            output = first - second
            stack.push(output)
        else:
            stack.push(int(element))
    return stack.pop()

#In this case, we push 4 then 12 to the stack
#Then we see + and do the result of 4 and 12 to be 16
#Once we see 16, we then push 16 to the stack
#Now the stack has 16
#Moving forward we push 4 to the stack again
#Now we have 16 and 4 in the stack
#We take the final result first / second and push that to the stack
#Stack now only has 4
#Return stack.pop which gives us the final result
print(evaluate_post_fix(["4","12","+", "4", "/"]))

print(evaluate_post_fix(["1", "13", "*", "5", "*", "5", "/"]))