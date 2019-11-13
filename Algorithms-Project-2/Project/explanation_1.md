### Problem 1 - LRU Cache

### Explanation

The LRU Cache is supposed to hold and store any type of key and its values, I chose a dictionary to store the key value pairs. The benefit of this is that lookup is in constant time. In addition, I used a doubly linkedlist to find the head and the tail as well as perform add and remove functionality on the linkedlist.

### Efficiency

Get in dictionary on average is in O(1) time however, in the worst case that can take O(n) time. In addition, in the set function, the average time will be constant O(1) but at times this can become O(n). Removing a node from the linkedlist and adding a node from the linkedlist will take constant O(1) time

### Problem 2 - File Recursion

### Explanation

I will be using a list to append to all the files that are found with the given extension name. Since we are going to be iterating over file and folders, this problem can be best solved via recursion. 

### Efficiency

Append has the time complexity of O(1) while Append has the time complexity of O(k)

### Problem 3 - Huffman Coding

### Explanation

### Efficiency



### Problem 4 - User in Group

### Explanation

Here we can use use recursion similar to how we check for path in File Recursion. We can check whether a user exists in the existing group. If not, we can check if there exists a group within a group and we can check there. At most each element will be checked atleast once

### Efficiency

The algorithm will run in O(n) time beacuse each group and user will be checked atleast once during the recursive calls.



