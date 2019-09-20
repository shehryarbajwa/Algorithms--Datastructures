class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0





def minimum_bracket_reversals(input_string):
    #First we check what the length of the input string is. If the input string is odd, then we return -1
    if len(input_string) % 2 == 1 :
        return -1
    
    #We create a temporary stack 
    temp_stack = Stack()
    count = 0
    #Traverse through the input string
    for bracket in input_string:
        #If there are no elements in the stack, then you add the first one
        if temp_stack.is_empty():
            temp_stack.push(bracket)
        else:
            #The top element of the stack is the one we added for the first time
            top = temp_stack.top()
            #If the last element of the stack doesn't match with the traversed upon item, it could mean }{, then we need to check
            #if the last item in the stack was an opening brace
            #If it is an opening brace and it doesnt match with the next element i.e element being traversed, then it means it is a balanced 
            #parenthesis
            #Since it is balanced, we can remove the top element from the stack and continue

            if top != bracket:
                if top == '{':
                    temp_stack.pop()
                    continue
            temp_stack.push(bracket)
    
    #Traverse through the stack while it has elements
    while not temp_stack.is_empty():
        first = temp_stack.pop()
        second = temp_stack.pop()
        if first == second and second == first:
            count += 1
        #Else in a situation like }{, we need to reverse both the brackets so it will take 2 reversals
        elif first == '{' and second == '}':
            count += 2
    return count



print(minimum_bracket_reversals("}}}{{{"))