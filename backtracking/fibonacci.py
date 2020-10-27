#In recursive functions, we should be thinking, how many new leaf nodes get created each iteration
#Time Complexity O(2 ^ n)
def fibonacci_number(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fibonacci_number_memoized(n, fib = {1:0, 2:1}):
    if n in fib:
        return fib[n]
    else:
        fib[n] = fibonacci_number_memoized(n - 1, fib) + fibonacci_number_memoized(n - 2, fib)
        return fib[n]
    
print(fibonacci_number_memoized(6))

    
