#nth Fibonacci

# Here the leaf nodes increase by 2^n
# Since for each child there are exactly 2 more fib calls
# Time Complexity : O(2^n)
# Space Complexity : O(n) using the function call stack, depending on the height of the tree

def nFibonacci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return nFibonacci(n-1) + nFibonacci(n-2)


print(nFibonacci(6))

#Time Complexity O(N)
#Space Complexity O(N) due to recursive calls
#Initializing the base case in memoize dictionary
def memoizationNFibonacci(n, memoize = {1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = memoizationNFibonacci(n -1, memoize) + memoizationNFibonacci(n - 2, memoize)


#Time Complexity O(N)
# Space Complexity O(1)

def iterativeNFibonacci(n):
    n1 = 0
    n2 = 1
    count = 0

    while count < n:
        next = n1 + n2
        n1 = n2
        n2 = next
        count += 1



