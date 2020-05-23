
class MinMaxStack:
    #Time Complexity O(1)
    #Space Complexity O(2N) which becomes O(N)
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    #Average amortized access and append in array list is O(1)
    #Time complexity O(1) Time
    #Space Complexity O(1)
    def peek(self):
        return self.stack[len(self.stack) - 1]

    #Time Complexity O(1)
    #Space Complexity O(1)
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    #Time Complexity O(1) - We are just appending at the end to both stacks
    #Space Complexity O(1)
    def push(self, number):
        new_min_max = {"min": number, "max": number}
        if len(self.minMaxStack) >= 1:
            last_min_max = self.minMaxStack[len(self.minMaxStack) - 1]
            new_min_max["min"] = min(last_min_max["min"], number)
            new_min_max["max"] = max(last_min_max["max"], number)
        self.minMaxStack.append(new_min_max)
        self.stack.append(number)

    #Time Complexity O(1) - Access last elements
    def get_minimum(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    #Time Complexity O(1) - Access last elements
    def get_maximum(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]