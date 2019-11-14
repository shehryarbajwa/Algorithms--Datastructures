### Problem 1 - LRU Cache

### Explanation

The LRU Cache is supposed to hold and store any type of key and its values, I chose a dictionary to store the key value pairs. The benefit of this is that lookup is in constant time. In addition, I used a doubly linkedlist to find the head and the tail as well as perform add and remove functionality on the linkedlist.

### Efficiency

Get in dictionary on average is in O(1) time however, in the worst case that can take O(n) time. In addition, in the set function, the average time will be constant O(1) but at times this can become O(n). Removing a node from the linkedlist and adding a node from the linkedlist will take constant O(1) time




