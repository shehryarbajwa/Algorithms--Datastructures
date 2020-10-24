#In recursive functions, we should be thinking, how many new leaf nodes get created each iteration
#Time Complexity O(2 ^ n)
def fibonacci_number(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

print(fibonacci_number(4))

    
