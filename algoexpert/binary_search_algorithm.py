# Binary Search Algorithm is like using a dictionary
# If you have a target, you look at the middle element, if target<middle then recurse left else recurse right

# Pre-requisite : List of things have to be sorted


# Time Complexity O(logn) because we eliminate half the input logarithmically
# Space Complexity O(logn) because of recursive calls in the call stack


def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):

    if left > right:
        return -1

    middle = (left + right) // 2
    potential_match = array[middle]

    if target == potential_match:
        return middle
    elif target < potential_match:
        return binarySearchHelper(array, target, left, middle + 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)


# Iterative implementation
# Time Complexity O(logn)
# Space Complexity O(1) not storing anything just iterating
def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        potMatch = array[middle]

        if target == potMatch:
            return middle
        elif target < potMatch:
            right = middle - 1
        else:
            left = middle + 1

    return -1


print(binary_search([1, 2, 3, 4, 5, 6], 3))
print(binarySearch([1, 2, 3, 4, 5, 6], 3))
