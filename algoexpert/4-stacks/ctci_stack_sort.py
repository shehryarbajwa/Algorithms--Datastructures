
#Time Complexity O(N^2)
#Space Complexity O(N)

def sortStack(stack):
  tempStack = Stack()
  while not stack.isEmpty():
    poppedElement = stack.pop()
    while not tempStack.isEmpty() and poppedElement < tempStack.peek():
      stack.push(tempStack.pop())
    tempStack.push(poppedElement)
  while not tempStack.isEmpty():
    stack.push(tempStack.pop())