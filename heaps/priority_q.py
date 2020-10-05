import heapq
def priority(array):
    heapq.heapify(array)
    return array

print(priority([8,4,7,2,3,4,5]))
#            8
#          /  \
#         4    7
#        / \  / \
#       2  3  4  5
#      
#            2
#          /   \ 
#         3     4
#        / \   / \
#       4   8  7  5 
# Python heapp smallest element has the highest priority
# Heapify doesn't sort the array just makes a heap out of it.
