## Remember in a binary search the efficiency is O(logn) with base 2
## Lets walk through why
## array size   0   1   2   3   4   5   6   7   8
## iterations   0   1   2   2   3   3   3   3   4

##As can be seen when the array size doubles, the number of iterations double
# When array size is 2^0 = 1, iter is 1
# When array size is 2^1 = 2, iter is 2
# When array size is 2^2 = 4, iter is 3
# When array size is 2^3 = 8, iter is 4

# The efficiency is O(log n + 1) with log base 2
# In compsci it is assumed log base is 2 so we ignore base
# adding the 1 will not impact since run time is not influenced by single variables or lower order terms
# Therefore the run time will be O(log n)

# The equation that displays this relationship is 
# n * 1/2^s = 1


def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        mid_element = array[mid_index]

        if target == mid_element:
            return mid_index
        
        elif target < mid_element:
            end_index = array[mid_index - 1]
        
        else:
            start_index = array[mid_index + 1]
    return -1

print(binary_search([1,2,3,4,5,6,7,8], 7))


#Binary search via recursion

def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return 'The start index exceeds the end index. Please try again'
    
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
    
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)