#Special array is a recursive problem.
#If a special array can contain other special arrays, it can be done recursively.


# Time Complexity what is N?
# Space Complexity what is D?

# Time complexity is O(N)
# N refers to all the elements including the elements in the sub-array

# Space Complexity is O(D) since D refers to the depth of sub-arrays

def product_sum(arr, multiplier=1):

    if len(arr) == 0:
        return
    sum = 0
    for element in arr:
        if type(element) == list:
            sum += product_sum(element, multiplier + 1)
        else:
            sum += element

    return sum * multiplier

#In the naive implementation, we are not taking care of the multiplier

def product_sum_arr_naive(arr):

    if len(arr) == 0:
        return

    sum = 0
    for element in arr:
        if type(element) == list:
            sum += product_sum(element)
        else:
            sum += element
    
    return sum


print(product_sum([1,2,3,[4,5]]))