### Problem 3 - Huffman Coding

### Explanation

We use a hash map to collect character frequencies and then convert the hash map into a sorted list. And then we create a HuffNode which will hold the character and frequencies of the characters in the original text string. The Node will also have references to the left child and the right child. 

### Efficiency

Creating an element frequency list will be done in O(n^2) time. It will be done in linear time since each key will be updated frequently. 
sort_node_frequencies will be done using Timsort by Python's built in sorting algorithm which runs in O(n log n) time
Constructing the huff_tree will take O(n^2) + O(n log n)
Assigning codes in the huff tree will be done via recursion, so O(n) for tree traversal
In our hash function, we map 0 and 1 to the same key multiple times depending on the position of the node in the tree. This will be done in O(n) time since each key will be updated frequently. So our assigning codes function will take O(n) + O(n) time
Decode next element will be done in O(n) time since we are going to traverse through the tree and return the character associated with the tree based on going left(0) or right(1) of the tree
Huffman encoding the tree will be done in O(nlogn) time for mapping each element to the data string
Huffman decoding will be done in O(n^2) since the while loop will be run n times i.e len of data and the while loop will then run decode_next element which will take O(n) time