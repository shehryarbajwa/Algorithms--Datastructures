### Problem 6 - List union & intersection

### Explanation

We will transform the linkedlist from a linkedlist to a python list. After creating a python list, we will create a mathematical set to hold the values from both lists and merge them together.

### Efficiency

Appending to a list will take O(1) time. In addition, node search will be in O(n) time. When we do the union of the two linked lists, we will convert the linkedlist 1 and linkedlist 2 to a python list and then iterate over the newly created list with the sets and add values to it. Insertion in array will take O(n) time.

When we create the intersection, we create two lists from each linkedlist. Then we iterate over one set and check for that element in set 2. If it is present in both then we append it to the newly created intersection list. Iterating over both sets and appending to the intersection list each element will take O(n^2) time