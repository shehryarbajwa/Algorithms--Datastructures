#Time Complexity O(2^n)
#Space Complexity O(n)
def nth_fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n-2)

#Time Complexity O(N)
#Space Complexity O(N)
def nth_fibonacci(n, memoize={1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = nth_fibonacci(n - 1, memoize) + nth_fibonacci(n - 2, memoize)
        return memoize[n]

#Time Complexity O(N)
#Space Complexity O(1)

def nth_fibonacci(n):
    last_two = [0,1]
    counter = 3

    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return 

