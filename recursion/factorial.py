#Factorial is a classic example of recursion. We can solve for the factorial of any given number by first solving
#for the factorial of the next smallest number and the next smallest number and so on

def factorial(n):
    if(n >= 1):
        return n * factorial(n - 1)
    else:
        return 1

#Lets take an example of the factorial 5

#   In our first iteration, since n is > 1, we will return 5 * factorial(4).
#   Before we run the else loop, now we will run the factorial function again
#   At 4 it becomes 4 * factorial(3)
#   At 3 it becomes 3 * factorial(2)
#   At 2 it becomes 2 * factorial(1)
#   At 1 it becomes 1 * factorial(0)
#   So the first function to stop running is the factorial 0 which will return 1
#   Next we come back to factorial(1) = 1 * factorial(0) = 1 * 1 = 1
#   Next we come to      factorial(2) = 2 * factorial(1) = 2 * 1 = 2
#   Next we come to      factorial(3) = 3 * factorial(2) = 3 * 2 = 6
#   Next we come to      factorial(4) = 4 * factorial(3) = 4 * 6 = 24
#   Next we come to      factorial(5) = 5 * factorial(4) = 5 * 24 = 120
#   This is when the function ends

#   Recursion is the art of solving a larger problem by first solving the smaller problems
#   It needs a base case which will cease the function running
#   It goes deep, deep, deep, then comes back up incrementally

print(factorial(2))