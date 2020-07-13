#Time Complexity O(N)
#Space Complexity O(1)
def longest_common_prefix(array):

    if len(array) == 0:
        return("")
    if len(array) == 1:
        return array[0]

    prefix = array[0]
    prefix_length = len(prefix)

    for word in array[1:]:
        
        while prefix != array[0:prefix_length]:
            prefix = prefix[:prefix_length - 1]
            prefix_length -= 1

            if prefix_length == 0:
                return("")
    return prefix